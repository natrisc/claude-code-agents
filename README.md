# Claude Code Agents

**Turn Claude Code into a disciplined AI engineering team.**

Architecture reviews, QA automation, security checks, and release readiness — built directly into your development workflow.

| Feature                 | Standard AI Coding | AI Scrum Team |
| ----------------------- | ------------------ | ------------- |
| Code generation         | ✔                  | ✔             |
| Architecture governance | ✖                  | ✔             |
| QA validation           | ✖                  | ✔             |
| Security review         | ✖                  | ✔             |
| Sprint memory           | ✖                  | ✔             |

---

## How It Works

```text
Feature request
      ↓
  Architect
      ↓
  Developer
      ↓
     QA
      ↓
  Security
      ↓
Release decision
```

Agents communicate through **canonical documents** in the repository — not through conversation. Each sprint follows a strict gate-based progression enforced by the Scrum Master. No agent guesses; no context is lost between sessions.

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

> "Initialize sprint-01"

Full setup instructions: [docs/setup.md](docs/setup.md)

---

## Core Concepts

- **Repository-centric memory** — agents read and write files, not conversation history
- **Role boundaries** — 10 specialist agents, each owning specific artifacts
- **Gate progression** — work cannot proceed until the previous gate is validated by `validate_gate.py`
- **Multi-sprint continuity** — product context, architecture, and analysis persist across sprints

---

## Documentation

| Topic | Link |
| --- | --- |
| Setup guide | [docs/setup.md](docs/setup.md) |
| Core concepts | [docs/concepts.md](docs/concepts.md) |
| Memory bank architecture | [docs/memory-bank.md](docs/memory-bank.md) |
| AI Scrum team roles | [docs/roles.md](docs/roles.md) |
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
