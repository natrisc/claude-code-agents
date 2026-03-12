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

- inconsistent architecture
- missing tests
- security blind spots
- no audit trail
- fragile codebases that accumulate AI debt

The root cause is that AI assistants have no memory, no role boundaries, and no workflow discipline. Every prompt starts from scratch.

---

## The Solution

This repository implements a **repository-centric AI Scrum team** for Claude Code.

Instead of relying on conversation context, agents communicate through **canonical documents** stored in the repository. Each agent reads specific input artifacts, writes to owned output artifacts, and the system enforces gate progression before any work proceeds.

The result is a **structured delivery system** with:

- clear role boundaries and ownership
- artifact-driven workflow state
- enforced gate progression
- escalation handling
- a full event log and sprint dashboard

---

## How It Works

### The Memory Bank

The core of the system is `memory-bank/` — a structured folder that serves as the shared memory of the AI team.

```text
memory-bank/
  context/        ← project context (Product Owner — immutable for others)
  planning/       ← roadmap, epics, backlog, sprint intent
  analysis/       ← requirements, business rules, edge cases
  architecture/   ← architecture, API contracts, data model, ADRs
  delivery/       ← frontend, backend, devops delivery notes
  quality/        ← test strategy, test report, security review
  reviews/        ← sprint review, PO decision
  state/          ← workflow_state.yaml, artifact_registry.yaml, dashboard.md
  tasks/          ← TASK-NNN.md files per routed piece of work
  escalations/    ← ESC-NNN.md files for unresolved blockers
  logs/           ← append-only event log
```

Every agent reads its required inputs from here and writes its outputs back here. Nothing is held in conversation context.

### Gate Progression

Work proceeds through a strict left-to-right state machine:

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

The Scrum Master reads `workflow_state.yaml` before routing any work. If a gate is not satisfied, work does not proceed.

### Task Tracking

Every time the Scrum Master routes work to a specialist, it creates a `TASK-NNN.md` file. The specialist updates it when they start and when they finish. The Scrum Master tracks all active tasks in `workflow_state.yaml` and regenerates `state/dashboard.md` after every state change.

### Escalation Handling

If any agent cannot proceed due to ambiguity or missing information, it raises an `ESC-NNN.md` escalation. The downstream work is blocked until the Product Owner resolves it. No agent may guess or work around an escalation.

---

## The AI Scrum Team

| Role | Owns | Reads |
| --- | --- | --- |
| Product Owner | `context/*`, `reviews/po_decision.md` | everything |
| Product Manager | `planning/roadmap.md`, `epics.md`, `backlog.md` | context |
| Scrum Master | `planning/sprint_intent.md`, `state/*`, `tasks/*` | everything |
| Business Analyst | `analysis/*` | context, planning |
| System Architect | `architecture/*` | context, analysis |
| Frontend Developer | `delivery/frontend_delivery.md` | context, analysis, architecture |
| Backend Developer | `delivery/backend_delivery.md` | context, analysis, architecture |
| DevOps Engineer | `delivery/devops_delivery.md` | architecture, delivery |
| QA Tester | `quality/test_strategy.md`, `quality/test_report.md` | analysis, delivery |
| Security Officer | `quality/security_review.md`, `quality/threat_model.md` | architecture, analysis, quality |

Role boundaries are strict. No agent edits artifacts owned by another role.

---

## Example Sprint

User request: Add OAuth login with Google.

### Step 1 — Context

Product Owner defines goals, constraints, and acceptance criteria in `context/project_context.md`. Sets `context_ready: true`.

### Step 2 — Planning

Product Manager writes roadmap, epics, and backlog items. Scrum Master writes sprint intent. Gate: `planning_complete: true`.

### Step 3 — Analysis

Business Analyst derives requirements, business rules, and edge cases from context and planning. Gate: `analysis_complete: true`.

### Step 4 — Architecture

System Architect designs OAuth flow, token handling, API contracts. Creates ADR. Gate: `architecture_complete: true`.

### Step 5 — Implementation *(parallel)*

Backend Developer implements OAuth service. Frontend Developer builds login UI. Both update their TASK files. Gate: `implementation_complete: true`.

### Step 6 — Quality *(parallel)*

QA Tester validates against requirements. Security Officer reviews token handling and secrets exposure. Gates: `qa_complete: true`, `security_complete: true`.

### Step 7 — Sprint Review

Scrum Master opens sprint review. Product Owner accepts, rejects, or requests changes. Gate: `po_decision_made: true`.

---

## Repository Structure

```text
.
├── CLAUDE.md                  ← operating model
├── README.md
├── .mcp.json                  ← external system integrations
├── memory-bank/               ← shared agent memory
│   ├── context/
│   ├── planning/
│   ├── analysis/
│   ├── architecture/
│   ├── delivery/
│   ├── quality/
│   ├── reviews/
│   ├── state/
│   ├── tasks/
│   ├── escalations/
│   └── logs/
└── .claude/
    ├── settings.json          ← permissions and guardrails
    ├── agents/                ← 9 specialist agent definitions
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

## Setup

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Clone this repository into your project

```bash
git clone https://github.com/natrisc/claude-code-agents .claude-agents
```

Or copy the relevant files into your existing project.

### 3. Make hooks executable

```bash
chmod +x .claude/hooks/*.sh
```

### 4. Start Claude

```bash
claude
```

### 5. Fill in the project context

Open `memory-bank/context/project_context.md` and complete the template. Then set its status to `accepted` in `memory-bank/state/artifact_registry.yaml`. This opens the first gate and starts the workflow.

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
- AI development workflow audits
- Agentic SDLC design and implementation

Contact: [coen@appvia.io](mailto:coen@appvia.io)

---

## License

MIT
