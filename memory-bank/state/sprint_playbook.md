# Sprint Playbook

Reference procedures for the Scrum Master. Read this file when initialising or closing a sprint.

---

## Sprint initialisation

When starting a new sprint (e.g. `sprint-01`):

1. Copy `memory-bank/sprints/SPRINT-TEMPLATE/` to `memory-bank/sprints/sprint-NNN/`
2. Replace `{sprint}` placeholders in each copied file with the sprint ID
3. Set `current_sprint: sprint-NNN` in `workflow_state.yaml`
4. Reset all gates to `false` in `workflow_state.yaml`
5. Add sprint artifact entries to `artifact_registry.yaml`:

```yaml
sprints/sprint-NNN/plan.md:
  owner: system_architect
  status: draft
  depends_on: [analysis/requirements.md, sprints/sprint-NNN/intent.md]

sprints/sprint-NNN/intent.md:
  owner: scrum_master
  status: draft
  depends_on: [planning/backlog.md, context/project_context.md]

sprints/sprint-NNN/delivery/frontend.md:
  owner: frontend_developer
  status: draft
  depends_on: [sprints/sprint-NNN/plan.md, sprints/sprint-NNN/intent.md]

sprints/sprint-NNN/delivery/backend.md:
  owner: backend_developer
  status: draft
  depends_on: [sprints/sprint-NNN/plan.md, sprints/sprint-NNN/intent.md]

sprints/sprint-NNN/delivery/devops.md:
  owner: devops_engineer
  status: draft
  depends_on: [sprints/sprint-NNN/delivery/backend.md, sprints/sprint-NNN/delivery/frontend.md]

sprints/sprint-NNN/quality/test_strategy.md:
  owner: qa_tester
  status: draft
  depends_on: [analysis/requirements.md, sprints/sprint-NNN/intent.md]

sprints/sprint-NNN/quality/test_report.md:
  owner: qa_tester
  status: draft
  depends_on: [sprints/sprint-NNN/quality/test_strategy.md, sprints/sprint-NNN/delivery/backend.md, sprints/sprint-NNN/delivery/frontend.md]

sprints/sprint-NNN/quality/security_review.md:
  owner: security_officer
  status: draft
  depends_on: [sprints/sprint-NNN/plan.md, sprints/sprint-NNN/quality/test_report.md]

sprints/sprint-NNN/quality/threat_model.md:
  owner: security_officer
  status: draft
  depends_on: [architecture/architecture.md, analysis/data_requirements.md]

sprints/sprint-NNN/review.md:
  owner: scrum_master
  status: draft
  depends_on: [sprints/sprint-NNN/delivery/frontend.md, sprints/sprint-NNN/delivery/backend.md, sprints/sprint-NNN/delivery/devops.md, sprints/sprint-NNN/quality/test_report.md, sprints/sprint-NNN/quality/security_review.md]

sprints/sprint-NNN/po_decision.md:
  owner: product_owner
  status: draft
  depends_on: [sprints/sprint-NNN/review.md]
```

6. Set `current_sprint: sprint-NNN` in `state/product_progress.yaml`
7. Append to `logs/events.log`: `YYYY-MM-DDTHH:MMZ  scrum_master  opened  sprints/sprint-NNN`
8. Regenerate dashboard:
   ```
   python workflow/scripts/regenerate_dashboard.py
   ```

---

## Routing work (per specialist)

Before routing any specialist:

1. Run the gate validator for the gate you need to be satisfied:
   ```
   python workflow/scripts/validate_gate.py <gate_name>
   ```
   If FAIL: do not route. Show failures and create a remediation task.

2. Create `memory-bank/tasks/TASK-NNN.md` from `memory-bank/tasks/TASK-TEMPLATE.md`
3. Fill all fields — no placeholder text

---

## Accepting specialist work

After a specialist reports they are done:

1. Validate the task file:
   ```
   python workflow/scripts/validate_task.py memory-bank/tasks/TASK-NNN.md
   ```
   If FAIL: return failures to the specialist. Do not accept.

2. Validate the target gate:
   ```
   python workflow/scripts/validate_gate.py <gate_name>
   ```
   If FAIL: do not set the gate flag to `true`. Show failures.
   If PASS: set `<gate_name>: true` in `workflow_state.yaml`.

3. Set artifact status to `accepted` in `artifact_registry.yaml`
4. Set task and role status to `done` in `workflow_state.yaml`
5. Append to `logs/events.log`: `YYYY-MM-DDTHH:MMZ  role  accepted  artifact`
6. Regenerate dashboard:
   ```
   python workflow/scripts/regenerate_dashboard.py
   ```

---

## Sprint close

After the Product Owner completes `sprints/{sprint}/po_decision.md`:

1. Validate the final gate:
   ```
   python workflow/scripts/validate_gate.py po_decision_made
   ```

2. Append to `state/product_progress.yaml`:

```yaml
sprint_history:
  sprint-NNN:
    goal: "<sprint goal>"
    outcome: accepted | accepted_with_actions | rejected
    completed_items: []
    carry_over_items: []
    context_changed: false
    context_version_after: ""
```

3. Update epic `status` and `completed_in_sprints` in `product_progress.yaml`
4. Update release `progress` percentage in `product_progress.yaml`
5. Move carry-over items to `planning/backlog.md` with disposition note
6. Append to `logs/events.log`: `YYYY-MM-DDTHH:MMZ  product_owner  closed  sprints/sprint-NNN outcome:accepted`
7. Regenerate dashboard:
   ```
   python workflow/scripts/regenerate_dashboard.py
   ```

---

## Escalation — raise

1. Create `memory-bank/escalations/ESC-NNN.md` from template
2. Fill `Blocked tasks` with TASK-NNN IDs that are paused
3. Set role status to `blocked` in `workflow_state.yaml`
4. Set task status to `blocked` in `TASK-NNN.md`
5. Add escalation to `blockers` list in `workflow_state.yaml`
6. Append to `logs/events.log`: `YYYY-MM-DDTHH:MMZ  role  raised  escalations/ESC-NNN.md`
7. Regenerate dashboard:
   ```
   python workflow/scripts/regenerate_dashboard.py
   ```
8. Route to product-owner

## Escalation — resolve

1. Set escalation `Status` to `resolved` in `ESC-NNN.md`
2. Remove from `blockers` in `workflow_state.yaml`
3. Set blocked role and task status back to `in_progress`
4. Append to `logs/events.log`: `YYYY-MM-DDTHH:MMZ  product_owner  resolved  escalations/ESC-NNN.md`
5. Regenerate dashboard:
   ```
   python workflow/scripts/regenerate_dashboard.py
   ```
