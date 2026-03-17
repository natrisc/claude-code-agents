# Workflow and Gate System

## Core principle

**Agents do not complete work. Validators complete work.**

Gates advance only when `workflow/scripts/validate_gate.py` returns PASS — not when an agent says it is done. See [Enforcement Layer](enforcement.md) for the full technical reference.

---

## Gate Progression

Work proceeds through a strict gate-based state machine. No gate can open unless the previous gate is already open and its artifact contract is satisfied.

```text
CONTEXT_READY
  → PLANNING_COMPLETE
  → ANALYSIS_COMPLETE
  → ARCHITECTURE_COMPLETE
  → IMPLEMENTATION_COMPLETE
  → QA_COMPLETE + SECURITY_COMPLETE  (both required; run in parallel)
  → SPRINT_REVIEW_READY
  → PO_DECISION_MADE
```

`QA_COMPLETE` and `SECURITY_COMPLETE` are independent and can proceed in parallel once `IMPLEMENTATION_COMPLETE` is open (`SECURITY_COMPLETE` can start as soon as `ARCHITECTURE_COMPLETE` is open).

---

## Default Delivery Flow (per sprint)

1. SM initialises `sprints/sprint-NNN/` from template, sets `current_sprint` in `workflow_state.yaml`
2. PO confirms context is current → SM runs validator → `context_ready: true`
3. SM writes `sprints/sprint-NNN/intent.md` → SM runs validator → `planning_complete: true`
4. BA writes/updates analysis artifacts → SM runs validator → `analysis_complete: true`
5. Architect writes/updates architecture artifacts and `plan.md` → SM runs validator → `architecture_complete: true`
6. FE + BE implement sprint scope → SM runs validator → `implementation_complete: true`
7. QA and Security write sprint quality artifacts → SM runs validators → `qa_complete: true`, `security_complete: true`
8. SM opens sprint review → `sprint_review_ready: true`
9. PO writes `sprints/sprint-NNN/po_decision.md` → `po_decision_made: true`
10. SM closes sprint: updates `product_progress.yaml`, moves carry-overs to backlog, regenerates dashboard

---

## Task Tracking

The Scrum Master creates `TASK-NNN.md` when routing work. Each task has a fixed set of required fields:

- `Owner`, `Sprint`, `Status`, `Created`, `Started`, `Completed`
- `Objective` — one sentence
- `Input artifacts` — what must be accepted before starting
- `Output artifacts` — what this task produces
- `Blocked by` — ESC-NNN references or `none`
- `Evidence` — filled when marking done; confirms output artifacts exist

Valid statuses: `queued` → `in_progress` → `done` (or `blocked` at any point).

The Scrum Master runs `validate_task.py` after every agent reports completion. A task is not accepted until the validator returns PASS.

All active tasks are tracked in `workflow_state.yaml`. The dashboard is regenerated after every state change via `python workflow/scripts/regenerate_dashboard.py`.

---

## Escalation Handling

If any agent cannot proceed due to ambiguity or missing information:

1. Create `memory-bank/escalations/ESC-NNN.md` from the template
2. Fill `Blocked tasks` with TASK-NNN IDs that are paused
3. Set role status to `blocked` in `workflow_state.yaml`
4. Set task status to `blocked` in `TASK-NNN.md`
5. Add escalation to `blockers` in `workflow_state.yaml`
6. Regenerate dashboard
7. Route to the Product Owner for resolution

No agent may guess, invent requirements, or work around an escalation. The only legal response to a blocker is to create an escalation and stop.

---

## Skills

Eleven reusable workflow skills are included:

| Skill | Purpose |
| --- | --- |
| `backlog-refinement` | convert rough ideas into Scrum-ready items |
| `story-writing` | produce user stories with testable acceptance criteria |
| `sprint-planning` | turn backlog items into a sprint-ready plan |
| `api-design` | design or review API contracts |
| `architect-review` | review changes for architectural fit |
| `back-end-implementation` | implement backend work with service boundaries and tests |
| `front-end-implementation` | implement frontend work with component boundaries and tests |
| `qa-regression` | review changes for regression risk and missing coverage |
| `security-review` | review for auth, validation, secret, and exposure risks |
| `release-readiness` | evaluate whether a change is safe to release |
| `incident-triage` | triage production issues across app, infra, and dependencies |
