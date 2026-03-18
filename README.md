# Claude Code Agents

**Turn Claude Code into a disciplined AI engineering team.**

Most AI coding tools are stateless. Every session starts from scratch — no memory of past decisions, no role boundaries, no delivery discipline. The result is architectural drift, missing tests, and security blind spots that compound across sprints.

This repository gives Claude Code a structured Scrum operating model: 9 specialist agents, formal gate progression, and a shared memory bank that persists across the full product lifecycle.

| Feature                    | Standard AI Coding | AI Scrum Team |
| -------------------------- | ------------------ | ------------- |
| Code generation            | ✔                  | ✔             |
| Architecture governance    | ✖                  | ✔             |
| QA validation              | ✖                  | ✔             |
| Security review            | ✖                  | ✔             |
| Multi-sprint memory        | ✖                  | ✔             |
| Formal change control      | ✖                  | ✔             |
| Role boundaries            | ✖                  | ✔             |

---

## How It Works

Nine specialist agents collaborate through canonical documents in the repository — not through conversation. No agent starts work until the previous gate is validated. No context is lost between sessions.

```text
Product Owner        → defines and owns project context
Product Manager      → roadmap, epics, backlog, release plan
Business Analyst     → requirements, business rules, edge cases
System Architect     → architecture, API contracts, data model, sprint plan
Backend Developer    → services, APIs, persistence, tests
Frontend Developer   → components, client logic, accessibility, tests
QA Tester           → test strategy, execution, release confidence
Security Officer    → threat model, security review, release blocker
DevOps Engineer     → CI/CD, deployment, monitoring, rollback
```

The Scrum Master orchestrates the full workflow — routing tasks, enforcing gates, and validating completion. Agents communicate through `memory-bank/` — a shared document store that spans every sprint.

---

## Quick Start

```bash
# 1. Install Claude Code
npm install -g @anthropic-ai/claude-code

# 2. Clone this repository
git clone https://github.com/natrisc/claude-code-agents
cd claude-code-agents

# 3. Install Python dependencies
pip install pyyaml

# 4. Make hooks and scripts executable
chmod +x .claude/hooks/*.sh
chmod +x workflow/scripts/*.py

# 5. Start Claude
claude
```

Then ask Claude:

> "Activate the project"

The Scrum Master will route a task to the Product Owner, who will define the project context. From there, the team takes over — breakdown, analysis, architecture, implementation, QA, security, and delivery.

Full setup instructions: [docs/setup.md](docs/setup.md)

---

## Core Concepts

- **Repository-centric memory** — agents read and write files, not conversation history. Context survives session boundaries.
- **9 specialist agents** — each owns specific artifacts and reads only what it needs. Role boundaries are enforced, not suggested.
- **Gate progression** — no phase begins until the previous gate passes `validate_gate.py`. Agents cannot skip steps.
- **Multi-sprint continuity** — product context, architecture, and analysis persist across sprints and evolve through formal change control.
- **Escalation over guessing** — when any agent encounters ambiguity, it raises an escalation. No agent invents requirements.

---

## Documentation

| Topic | Link |
| --- | --- |
| Setup guide | [docs/setup.md](docs/setup.md) |
| Core concepts | [docs/concepts.md](docs/concepts.md) |
| Memory bank | [docs/memory-bank.md](docs/memory-bank.md) |
| Roles | [docs/roles.md](docs/roles.md) |
| Workflow & gate system | [docs/workflow.md](docs/workflow.md) |
| Enforcement layer | [docs/enforcement.md](docs/enforcement.md) |
| Architecture | [docs/architecture.md](docs/architecture.md) |
| Git workflow | [docs/git-workflow.md](docs/git-workflow.md) |
| MCP integrations | [docs/integrations.md](docs/integrations.md) |
| Roadmap | [docs/roadmap.md](docs/roadmap.md) |

---

## Contributing

Contributions welcome.

- follow the operating model in `CLAUDE.md`
- keep changes small and focused
- update relevant memory-bank artifacts if behaviour changes
- security guidelines apply to all contributions

---

## Need Help?

I help engineering teams implement structured AI delivery workflows using Claude Code.

- Claude Code workflow setup for your codebase
- AI development workflow design and implementation
- Agentic SDLC consulting

Contact: [coen@appvia.nl](mailto:coen@appvia.nl)

---

⭐ If this project helps you, please star the repository.

---

## License

MIT
