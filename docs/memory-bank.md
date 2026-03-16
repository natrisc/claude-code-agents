# Memory Bank

The memory bank is the shared communication layer for all agents. Agents never rely on conversation context — they read and write canonical documents in this directory tree.

## Structure

```text
memory-bank/
  context/          ← project context (Product Owner — immutable for others)
  planning/         ← roadmap, epics, backlog, release plan
  analysis/         ← requirements, business rules, edge cases (spans sprints)
  architecture/     ← architecture, API contracts, data model, ADRs (spans sprints)
  sprints/
    SPRINT-TEMPLATE/  ← copied to start each new sprint
    sprint-01/
      intent.md
      delivery/     ← frontend.md, backend.md, devops.md
      quality/      ← test_strategy.md, test_report.md, security_review.md
      review.md
      po_decision.md
  state/            ← workflow_state.yaml, artifact_registry.yaml,
  │                    product_progress.yaml, dashboard.md
  tasks/            ← TASK-NNN.md per piece of routed work
  escalations/      ← ESC-NNN.md for unresolved blockers
  logs/             ← append-only event log
```

## Ownership Rules

- `context/` is owned by the Product Owner and immutable for all other agents
- `planning/` is owned by the Product Manager
- `analysis/` is owned by the Business Analyst and spans sprints
- `architecture/` is owned by the System Architect and spans sprints
- `sprints/sprint-NNN/` artifacts are owned by the respective specialist role
- `state/` is owned and maintained by the Scrum Master

No agent edits artifacts owned by another role.

## Product Progress

`state/product_progress.yaml` tracks the full product lifecycle across sprints:

```yaml
epics:
  E-01:
    title: User authentication
    status: in_progress
    completed_in_sprints: [sprint-01]

releases:
  MVP:
    target_epics: [E-01, E-02]
    progress: 45

sprint_history:
  sprint-01:
    outcome: accepted
    completed_items: [ITEM-001, ITEM-002]
    carry_over_items: [ITEM-003]
```
