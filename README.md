# AI Scrum Team

This repository provides a structured setup for running **Claude Code as an AI-powered Scrum team** inside a software project.

Instead of treating Claude as a single coding assistant, this repository organizes Claude into **specialized roles** that mirror a real Scrum team:

- Product Owner
- Product Manager
- Business Analyst
- System Architect
- Frontend Developer
- Backend Developer
- QA Tester
- Security Officer
- DevOps Engineer

The main Claude session acts as the **Scrum Master**, orchestrating the work of these roles.

The goal is to improve:

- engineering discipline
- architectural consistency
- security awareness
- test coverage
- release readiness

while maintaining **fast AI-assisted development workflows**.

---

# Architecture

The repository uses Claude Code's extensibility features:

- `CLAUDE.md` → repository operating model
- `.claude/settings.json` → permissions and hooks
- `.claude/agents` → specialized roles
- `.claude/skills` → reusable workflows
- `.claude/rules` → engineering standards
- `.claude/hooks` → automated guardrails
- `.mcp.json` → connections to external systems

```

.
├── CLAUDE.md
├── README.md
├── .mcp.json
└── .claude
├── settings.json
├── agents
├── skills
├── rules
└── hooks

```

---

# AI Scrum Team Roles

Each role has a clearly defined responsibility.

## Scrum Master

The main Claude session.

Responsibilities:

- coordinate the work
- route tasks to the correct specialist
- ensure workflow discipline
- produce integrated outputs

---

## Product Owner

Responsible for:

- acceptance criteria
- scope control
- release acceptance

---

## Product Manager

Responsible for:

- prioritization
- business value
- roadmap alignment

---

## Business Analyst

Responsible for:

- domain modeling
- workflows
- dependencies
- business rules

---

## System Architect

Responsible for:

- architecture decisions
- module boundaries
- API contracts
- technical tradeoffs

---

## Frontend Developer

Responsible for:

- UI implementation
- React components
- accessibility
- frontend tests

---

## Backend Developer

Responsible for:

- APIs
- services
- persistence
- integration tests

---

## QA Tester

Responsible for:

- regression testing
- edge cases
- test completeness
- release confidence

---

## Security Officer

Responsible for reviewing:

- authentication
- authorization
- dependency risks
- input validation
- secrets handling

---

## DevOps Engineer

Responsible for:

- CI/CD
- infrastructure
- deployment safety
- rollback planning
- observability

---

# Development Workflow

The default workflow for new work is:

1. Clarify requirements
2. Refine backlog item
3. Define acceptance criteria
4. Evaluate architecture impact
5. Implement code
6. Add or update tests
7. Perform QA review
8. Perform security review
9. Validate release readiness

---

# Definition of Done

A task is complete when:

- acceptance criteria are satisfied
- code follows repository architecture
- tests exist or are updated
- lint and typecheck pass
- security concerns are addressed
- documentation updated if behavior changed
- release risks documented

---

# Hooks and Guardrails

Claude hooks enforce safety and consistency.

Current hooks include:

### PreToolUse

Prevents dangerous commands such as:

- `rm -rf /`
- `terraform destroy`
- `kubectl delete`

### PostToolUse

Runs formatting automatically after edits.

Examples:

- `prettier`
- `ruff`
- `rustfmt`

### TaskCompleted

Triggers a final review reminder that checks:

- changed files
- tests executed
- risks and follow-ups

---

# Security Model

Claude's shell access is restricted using `settings.json`.

Examples of blocked actions:

- reading `.env` files
- reading secrets directories
- editing production infrastructure
- destructive infrastructure commands

Potentially dangerous commands require confirmation.

---

# Supported Technology Stacks

This setup supports multiple stacks.

Typical combinations include:

- React + Node
- React + Python
- React + Rust
- Python backend services
- Rust backend services

Language-specific rules are located in:

```

.claude/rules/

```

Examples:

- `frontend.md`
- `backend.md`
- `python.md`
- `rust.md`
- `testing.md`
- `security.md`
- `devops.md`

---

# Repository Commands

Typical validation workflow:

Run tests:

```

npm test

```

Run formatting:

```

prettier --write

```

Run lint/typecheck:

```

turbo typecheck lint

```

Adjust commands depending on repository tooling.

---

# Claude Usage

Typical Claude interactions follow this pattern.

### Planning

```

QPLAN

```

Analyze the repository and propose an implementation plan.

---

### Implementation

```

QCODE

```

Implement the plan and run tests and checks.

---

### Code Review

```

QCHECK

```

Review the change as a skeptical senior engineer.

---

### Function Review

```

QCHECKF

```

Review modified or new functions.

---

### Test Review

```

QCHECKT

```

Review modified or new tests.

---

### UX Validation

```

QUX

```

Simulate a human UX tester and list important scenarios.

---

# Model Context Protocol (MCP)

The repository can connect Claude to external systems using MCP.

Typical integrations:

- GitHub
- Linear or Jira
- Notion or Confluence
- Postgres
- Figma
- Sentry
- Kubernetes
- cloud infrastructure

Configuration lives in:

```

.mcp.json

```

---

# Setup

1. Install Claude Code

```

npm install -g @anthropic-ai/claude-code

```

2. Clone the repository.

3. Ensure hooks are executable:

```

chmod +x .claude/hooks/*.sh

```

4. Start Claude from the project directory.

```

claude

```

---

# Goals of This Repository

This setup aims to create a development environment where:

- AI behaves like a disciplined engineering team
- architectural decisions are consistent
- security is considered automatically
- testing is integrated into development
- releases are safer

---

# Contributing

When contributing:

- follow repository architecture rules
- write or update tests
- maintain security discipline
- document behavior changes
- keep changes small and focused

---

# License

MIT