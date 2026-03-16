# Workflow and Gate System

## Gate Progression

Work proceeds through a strict gate-based state machine. The Scrum Master reads `workflow_state.yaml` before routing any work. If a gate is not satisfied, work does not proceed.

```text
CONTEXT_READY
  → PLANNING_COMPLETE
  → ANALYSIS_COMPLETE
  → ARCHITECTURE_COMPLETE
  → IMPLEMENTATION_COMPLETE
  → QA_COMPLETE + SECURITY_COMPLETE
  → SPRINT_REVIEW_READY
  → PO_DECISION_MADE
```

## Default Delivery Flow (per sprint)

1. SM initialises `sprints/sprint-NNN/` from template, sets `current_sprint` in `workflow_state.yaml`
2. PO confirms context is current → `context_ready: true`
3. SM writes `sprints/sprint-NNN/intent.md` → `planning_complete: true`
4. BA writes/updates analysis artifacts → `analysis_complete: true`
5. Architect writes/updates architecture artifacts → `architecture_complete: true`
6. FE + BE implement sprint scope → `implementation_complete: true`
7. QA and Security write sprint quality artifacts → `qa_complete` and `security_complete: true`
8. SM opens sprint review → `sprint_review_ready: true`
9. PO writes `sprints/sprint-NNN/po_decision.md` → `po_decision_made: true`
10. SM closes sprint: updates `product_progress.yaml`, moves carry-overs to backlog

## Task Tracking

When the Scrum Master routes work, it creates a `TASK-NNN.md` file. The agent updates it on start and completion. All active tasks are tracked in `workflow_state.yaml`. The dashboard is regenerated after every state change.

## Escalation Handling

If any agent cannot proceed due to ambiguity or missing information:

1. Create `memory-bank/escalations/ESC-NNN.md`
2. Set the role to `blocked` in `workflow_state.yaml`
3. Route to the Product Owner for resolution

No agent may guess, invent requirements, or work around an escalation.

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
