# Architecture

## Three-Level Delivery Model

The system separates three concerns:

| Level | What it answers | Artifacts |
| --- | --- | --- |
| **Product** | What are we building? | `context/`, `planning/roadmap.md`, `epics.md` |
| **Architecture** | How is it structured? | `analysis/`, `architecture/` |
| **Sprint** | What are we delivering now? | `sprints/sprint-NNN/` |

Sprint outputs never overwrite each other. Every sprint has its own folder with its own delivery, quality, review, and decision artifacts. The product context is immutable unless the Product Owner formally changes it with a version bump and change log entry.

## Repository Structure

```text
.
├── CLAUDE.md                  ← operating model
├── README.md
├── .mcp.json                  ← external system integrations
├── memory-bank/               ← shared agent memory
└── .claude/
    ├── settings.json          ← permissions and guardrails
    ├── agents/                ← 9 specialist agent definitions
    ├── skills/                ← 2 reusable workflow skills
    ├── rules/
    │   ├── shared/            ← engineering and testing rules (all coding agents)
    │   ├── roles/             ← role-specific rules (backend, frontend, devops, security, product)
    │   └── languages/         ← language-specific rules (python, rust)
    └── hooks/                 ← automated safety checks
```

## Guardrails

### Permissions

Claude's shell access is restricted in `settings.json`:

- blocked: `rm -rf /`, `terraform destroy`, `kubectl delete`, reading `.env` files
- confirmation required: `git push`, `terraform apply`, `kubectl apply`, `psql`
- permitted without asking: test runners, linters, formatters, read-only git commands

### Hooks

- **PreToolUse**: blocks dangerous shell commands before execution
- **PostToolUse**: runs formatters automatically after file edits
- **TaskCompleted**: triggers a final review checklist

## Example: Two Sprints Toward a Product

**Product context**: Build a device telemetry platform.

### Sprint 1 — Core ingestion pipeline

1. PO confirms product context. SM initialises `sprints/sprint-01/`
2. BA derives requirements for the ingestion scope
3. Architect designs the pipeline and data model
4. BE implements the ingestion service. FE builds the status dashboard
5. QA validates. Security reviews the data pipeline
6. SM opens sprint review. PO accepts with one carry-over item
7. SM closes sprint: updates epic progress, moves carry-over to backlog

### Sprint 2 — Alerting and notifications

1. SM initialises `sprints/sprint-02/` — sprint-01 history is preserved
2. BA updates requirements for alerting scope. Architect extends the data model
3. BE implements alert rules. FE adds notification UI
4. QA validates. Security reviews the alert dispatch path
5. PO accepts. Epic E-01 moves to `done` in `product_progress.yaml`

At any point: `state/dashboard.md` shows the full picture — gates, active tasks, epic progress, sprint history, recent events.
