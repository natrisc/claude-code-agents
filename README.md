# Claude Code Agents

**Turn Claude Code into a disciplined AI engineering team.**

Architecture reviews, QA automation, security checks, and release readiness — built directly into your development workflow.

⭐ If this project helps you, please star the repository.

---

## The Problem

Most developers use AI coding tools like this:

```text
"Write code for X."
```

The result is usually:

- inconsistent architecture across sprints
- missing tests
- security blind spots
- no audit trail
- AI drift — each session forgets what the last one decided

The root cause is simple: AI assistants have no memory, no role boundaries, and no workflow discipline. Every prompt starts from scratch.

---

## The Solution

This repository implements a **repository-centric AI Scrum team** for Claude Code.

Instead of relying on conversation context, agents communicate through **canonical documents** in the repository. Each agent reads its required input artifacts, writes to its owned output artifacts, and the system enforces gate-based progression before any work proceeds.

The product evolves across multiple sprints against one active product baseline — with formal change control, escalation handling, a full event log, and a live sprint dashboard.

---

## How It Works

### One Product, Many Sprints

The system separates three concerns:

| Level | What it answers | Artifacts |
| --- | --- | --- |
| **Product** | What are we building? | `context/`, `planning/roadmap.md`, `epics.md` |
| **Architecture** | How is it structured? | `analysis/`, `architecture/` |
| **Sprint** | What are we delivering now? | `sprints/sprint-NNN/` |

Sprint outputs never overwrite each other. Every sprint has its own folder with its own delivery, quality, review, and decision artifacts. The product context is immutable unless the Product Owner formally changes it with a version bump and change log entry.

### The Memory Bank

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

### Gate Progression

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

### Task Tracking

When the Scrum Master routes work, it creates a `TASK-NNN.md` file. The agent updates it on start and completion. All active tasks are tracked in `workflow_state.yaml`. The dashboard is regenerated after every state change.

### Product Progress

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

### Escalation Handling

If any agent cannot proceed due to ambiguity or missing information, it raises an `ESC-NNN.md` file. Downstream work is blocked until the Product Owner resolves it. No agent may guess or work around an escalation.

---

## The AI Scrum Team

| Role | Owns | Reads |
| --- | --- | --- |
| Product Owner | `context/*`, `sprints/{sprint}/po_decision.md` | everything |
| Product Manager | `planning/roadmap.md`, `epics.md`, `backlog.md` | context |
| Scrum Master | `sprints/{sprint}/intent.md`, `state/*`, `tasks/*` | everything |
| Business Analyst | `analysis/*` | context, planning |
| System Architect | `architecture/*` | context, analysis |
| Frontend Developer | `sprints/{sprint}/delivery/frontend.md` | context, analysis, architecture |
| Backend Developer | `sprints/{sprint}/delivery/backend.md` | context, analysis, architecture |
| DevOps Engineer | `sprints/{sprint}/delivery/devops.md` | architecture, delivery |
| QA Tester | `sprints/{sprint}/quality/test_*.md` | analysis, delivery |
| Security Officer | `sprints/{sprint}/quality/security_review.md` | architecture, analysis, quality |

Role boundaries are strict. No agent edits artifacts owned by another role.

---

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

---

## Repository Structure

```text
.
├── CLAUDE.md                  ← operating model
├── README.md
├── .mcp.json                  ← external system integrations
├── memory-bank/               ← shared agent memory
└── .claude/
    ├── settings.json          ← permissions and guardrails
    ├── agents/                ← 10 specialist agent definitions
    ├── skills/                ← 11 reusable workflow skills
    ├── rules/                 ← stack-specific engineering standards
    └── hooks/                 ← automated safety checks
```

---

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

---

## Git Workflow

This repository follows a **human-supervised AI delivery workflow**.

Claude helps plan, implement, review, and validate changes.  
A human developer remains responsible for final approval and merging.

### Who makes code changes?

Claude can:

- analyze requirements
- propose a plan
- implement code changes
- add or update tests
- review code quality
- review test quality
- suggest a commit message

A human developer is responsible for:

- deciding when work is ready
- reviewing the final diff
- approving commits and pushes
- opening and merging pull requests

### Who commits?

Default model:

- Claude prepares the change
- Claude may suggest a Conventional Commit message
- the human developer decides whether to commit
- the human developer decides whether to push

If you explicitly use the `QGIT` shortcut, Claude may:

1. stage changes
2. create a commit
3. push the branch

That workflow should be treated as **opt-in**, not automatic. The existing shortcut guidance already frames `QGIT` as the explicit command for staging, committing, and pushing. :contentReference[oaicite:0]{index=0}

### Branch Strategy

Use **short-lived feature branches**.

Recommended naming:

- `feat/<short-description>`
- `fix/<short-description>`
- `refactor/<short-description>`
- `chore/<short-description>`

Examples:

git checkout -b feat/linkedin-publishing
git checkout -b fix/instagram-timeout
git checkout -b refactor/publisher-abstraction
Default Change Flow

The recommended flow is:

Create a branch

Ask Claude to plan the change

Ask Claude to implement the change

Review the diff

Run checks and tests

Commit with a Conventional Commit message

Push the branch

Open a pull request

Review and merge

### In practice:

Create branch
→ QPLAN
→ QCODE
→ QCHECK
→ QCHECKT
→ review diff
→ commit
→ push
→ PR
→ merge

### Pull Request Workflow

Each meaningful change should go through a pull request.

A good PR should include:

what changed

why it changed

affected areas

tests run

known risks

rollout or migration notes if relevant

Claude can help draft this summary.

### Commit Message Format

Use Conventional Commits.

Examples:

feat(api): add linkedin publishing endpoint
fix(web): handle expired auth token redirect
refactor(shared): simplify social media validation
test(api): add publish failure integration coverage

Do not mention Claude or Anthropic in commit messages. That rule is already part of the repo guidance. 

CLAUDE

Merge Strategy

Prefer:

small pull requests

one logical change per PR

squash merge for cleanup when appropriate

Avoid:

long-running branches

mixing unrelated refactors with feature work

direct commits to main

Protected Branch Recommendation

Protect main with:

required PR review

required status checks

no force push

no direct push

Recommended required checks:

tests

lint

typecheck

any security or build checks used by the project

Release Flow

For release-sensitive changes:

complete implementation

run QCHECK

run QCHECKT

run release-readiness review

confirm rollback notes

merge via PR

deploy through normal CI/CD pipeline

Recommended Ownership Model

The cleanest model for teams is:

Claude owns implementation assistance

the engineer owns repository history

the team owns merge and release decisions

This keeps AI fast, while keeping git history and production responsibility under human control.

---

## Setup

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Clone this repository into your project

```bash
git clone https://github.com/natrisc/claude-code-agents
```

Or copy the `.claude/` and `memory-bank/` folders into an existing project.

### 3. Make hooks executable

```bash
chmod +x .claude/hooks/*.sh
```

### 4. Start Claude

```bash
claude
```

### 5. Fill in the project context

Open `memory-bank/context/project_context.md` and complete the template.
Set its status to `accepted` in `memory-bank/state/artifact_registry.yaml`.
This opens the first gate.

### 6. Start your first sprint

Ask Claude to initialise sprint-01. The Scrum Master will copy the sprint template, set the current sprint in `workflow_state.yaml`, and begin routing work.

---

## Supported Stacks

Engineering rules in `.claude/rules/` cover:

- TypeScript / Node
- React
- Python
- Rust
- REST APIs
- cloud-native and containerised systems

The system is stack-agnostic — rules are additive, not prescriptive.

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

---

## MCP Integrations

Connect Claude to external systems via `.mcp.json`:

- GitHub — issues, PRs, code search
- Linear or Jira — backlog management
- Postgres — live database queries
- Notion or Confluence — documentation
- Sentry — error tracking
- Kubernetes — cluster observability

---

## Roadmap

- [ ] Variant C — mandatory sign-off gates, invalidation enforcement, audit reports
- [ ] Stack-specific memory-bank presets
- [ ] GitHub Actions integration for gate enforcement
- [ ] Deeper MCP integrations for Linear and Sentry

---

## Contributing

Contributions welcome.

- follow the operating model in `CLAUDE.md`
- keep changes small and focused
- update relevant memory-bank artifacts if behaviour changes
- security guidelines apply to all contributions

---

## Need Help Setting This Up?

I help engineering teams implement structured AI delivery workflows using Claude Code.

Services:

- Claude Code workflow setup for your codebase
- AI development workflow design and implementation
- Agentic SDLC consulting

Contact: [coen@appvia.nl](mailto:coen@appvia.nl)

---

## License

MIT
