# Enforcement Layer

## Core principle

**Agents do not complete work. Validators complete work.**

An agent writing a file is not sufficient to advance a gate. The Scrum Master runs validator scripts that inspect artifacts and state. A gate only opens when the validator returns PASS.

---

## Components

### `workflow/contracts/gates.yaml`

Machine-readable gate contracts. For each gate, defines:

- `prerequisite_gates` — earlier gates that must already be open
- `required_files` — files that must exist and be non-empty under `memory-bank/`
- Optional flags: `task_list_nonempty`, `all_tasks_resolved`

Path token `{current_sprint}` is resolved at runtime from `workflow_state.yaml`.

### `workflow/scripts/validate_gate.py`

Reads `workflow_state.yaml` and `gates.yaml`. For a given gate, checks:

1. All prerequisite gates are open (flags `true` in `workflow_state.yaml`)
2. All required files exist and are non-empty under `memory-bank/`
3. Any structural conditions (e.g. tasks exist, all tasks resolved)

Returns `[PASS]` or `[FAIL]` with a list of failures.

```bash
# Validate a specific gate
python workflow/scripts/validate_gate.py planning_complete

# Validate all gates
python workflow/scripts/validate_gate.py --all
```

Exit code `0` = PASS, `1` = FAIL, `2` = usage or file error.

### `workflow/scripts/validate_task.py`

Validates a `TASK-NNN.md` file. Checks:

- Required header fields are present and not placeholder text: `Owner`, `Sprint`, `Status`, `Created`
- Required sections exist and have content: `Objective`, `Input artifacts`, `Output artifacts`
- `Evidence` section is filled when status is `done`
- `Status` is one of: `queued`, `in_progress`, `blocked`, `done`

```bash
# Validate a specific task
python workflow/scripts/validate_task.py memory-bank/tasks/TASK-001.md

# Validate all tasks
python workflow/scripts/validate_task.py --all
```

### `workflow/scripts/regenerate_dashboard.py`

Rebuilds `memory-bank/state/dashboard.md` from state files. Run after every state change — do not hand-write the dashboard.

```bash
python workflow/scripts/regenerate_dashboard.py
```

---

## Gate contracts

| Gate | Prerequisite gates | Required files |
| --- | --- | --- |
| `context_ready` | — | `context/project_context.md` |
| `planning_complete` | `context_ready` | `sprints/{current_sprint}/intent.md` |
| `analysis_complete` | `planning_complete` | all `analysis/*.md` |
| `architecture_complete` | `analysis_complete` | all `architecture/*.md`, `sprints/{current_sprint}/plan.md` |
| `implementation_complete` | `architecture_complete` | `sprints/{current_sprint}/delivery/backend.md`, `frontend.md`, `devops.md` |
| `qa_complete` | `implementation_complete` | `sprints/{current_sprint}/quality/test_strategy.md`, `test_report.md` |
| `security_complete` | `architecture_complete` | `sprints/{current_sprint}/quality/security_review.md`, `threat_model.md` |
| `sprint_review_ready` | `implementation_complete` + `qa_complete` + `security_complete` | `sprints/{current_sprint}/review.md` |
| `po_decision_made` | `sprint_review_ready` | `sprints/{current_sprint}/po_decision.md` |

The full contract with all fields is in `workflow/contracts/gates.yaml`.

---

## Scrum Master enforcement protocol

Before routing work to any specialist:

```
1. python workflow/scripts/validate_gate.py <required_gate>
   → FAIL: show failures, do not route
   → PASS: proceed
```

After a specialist reports completion:

```
1. python workflow/scripts/validate_task.py memory-bank/tasks/TASK-NNN.md
   → FAIL: return failures to specialist, do not accept
2. python workflow/scripts/validate_gate.py <target_gate>
   → FAIL: do not set gate flag to true
   → PASS: set gate flag to true in workflow_state.yaml
3. Set artifact status to accepted in artifact_registry.yaml
4. Set task status to done
5. python workflow/scripts/regenerate_dashboard.py
```

---

## Task contract

Every `TASK-NNN.md` must have these fields before it can be marked `done`:

| Field | Type | Notes |
| --- | --- | --- |
| `Owner` | header | role name |
| `Sprint` | header | sprint ID |
| `Status` | header | `queued` / `in_progress` / `blocked` / `done` |
| `Created` | header | YYYY-MM-DD |
| `Started` | header | YYYY-MM-DD or blank |
| `Completed` | header | YYYY-MM-DD or blank |
| `Objective` | section | one sentence |
| `Input artifacts` | section | paths that must be accepted before starting |
| `Output artifacts` | section | paths this task produces |
| `Blocked by` | section | ESC-NNN references or `none` |
| `Evidence` | section | filled when marking done — confirms output artifacts exist |

---

## Escalation rules

If any agent cannot proceed due to missing, ambiguous, or contradictory requirements:

1. Create `memory-bank/escalations/ESC-NNN.md` from the template
2. Fill `Blocked tasks` with the TASK-NNN IDs that are paused
3. Set role status to `blocked` in `workflow_state.yaml`
4. Set task status to `blocked` in `TASK-NNN.md`
5. Add escalation to `blockers` in `workflow_state.yaml`
6. Run `python workflow/scripts/regenerate_dashboard.py`
7. Route to product-owner

The only legal actions when blocked are: create escalation, set blocked state, stop routing downstream work. No agent may guess, invent requirements, or work around an escalation.

---

## Adding the enforcement layer to an existing project

1. Copy `workflow/` into your project
2. Install PyYAML: `pip install pyyaml`
3. Make scripts executable: `chmod +x workflow/scripts/*.py`
4. Verify your `workflow_state.yaml` gate flags match the keys in `gates.yaml`
5. Run `python workflow/scripts/validate_gate.py --all` — confirm `context_ready` passes if context is set up
6. Run `python workflow/scripts/regenerate_dashboard.py` — confirm dashboard generates cleanly
