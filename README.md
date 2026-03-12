# Claude Code Agents

**Agentic Delivery System for Claude Code**

Turn Claude Code into a disciplined AI engineering team with architecture reviews, QA automation, security checks, and release readiness built into the workflow.

⭐ If this project helps you, please consider starring the repository.

---

# What This Project Does

This repository transforms **Claude Code** into a **multi-agent software delivery system**.

Instead of treating Claude as a single coding assistant, this setup organizes Claude into **specialized engineering roles** coordinated by a Scrum-Master-style orchestrator.

Roles include:

• Product Owner  
• Product Manager  
• Business Analyst  
• System Architect  
• Frontend Developer  
• Backend Developer  
• QA Tester  
• Security Officer  
• DevOps Engineer  

The main Claude session acts as the **Scrum Master**, coordinating these agents to deliver structured, production-ready features.

The goal is to improve:

- engineering discipline
- architectural consistency
- security awareness
- test coverage
- release readiness

while maintaining **fast AI-assisted development workflows**.

---

# Example Workflow

User request:

> Add OAuth login with Google.

Claude workflow:

1. Product Owner defines acceptance criteria
2. Business Analyst models authentication flow
3. System Architect designs architecture changes
4. Backend Developer implements OAuth service
5. Frontend Developer integrates login UI
6. QA Tester creates authentication tests
7. Security Officer reviews token handling
8. DevOps Engineer validates deployment safety

Result: a **production-ready feature with tests and security review**.

---

# Why This Exists

Most developers currently use AI coding tools like this:

"Write code for X."

This often leads to:

- inconsistent architecture
- missing tests
- security vulnerabilities
- chaotic prompts
- fragile codebases

This repository introduces **structured AI collaboration**.

Claude behaves like a **disciplined engineering team** rather than a single coding assistant.

---

# System Architecture

The repository uses Claude Code's extensibility features:

- `CLAUDE.md` → repository operating model
- `.claude/settings.json` → permissions and guardrails
- `.claude/agents` → specialized AI roles
- `.claude/skills` → reusable workflows
- `.claude/rules` → engineering standards
- `.claude/hooks` → automated safety checks
- `.mcp.json` → external system integrations

Repository structure:

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

Each role has clearly defined responsibilities.

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

The default workflow for new work:

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

Typical combinations include:

- React + Node
- React + Python
- React + Rust
- Python backend services
- Rust backend services

Language-specific rules live in:

```

.claude/rules/

```

Examples include:

- `frontend.md`
- `backend.md`
- `python.md`
- `rust.md`
- `testing.md`
- `security.md`
- `devops.md`

---

# Setup

Install Claude Code:

```

npm install -g @anthropic-ai/claude-code

```

Clone the repository:

```

git clone [https://github.com/YOUR-REPO/claude-code-agents](https://github.com/YOUR-REPO/claude-code-agents)

```

Make hooks executable:

```

chmod +x .claude/hooks/*.sh

```

Start Claude from the project directory:

```

claude

```

---

# Usage

Typical Claude interactions follow this pattern.

### Planning

```

QPLAN

```

Analyze the repository and propose an implementation plan.

### Implementation

```

QCODE

```

Implement the plan and run tests and checks.

### Code Review

```

QCHECK

```

Review the change as a skeptical senior engineer.

### Function Review

```

QCHECKF

```

Review modified or new functions.

### Test Review

```

QCHECKT

```

Review modified or new tests.

### UX Validation

```

QUX

```

Simulate a human UX tester and list important scenarios.

---

# Model Context Protocol (MCP)

Claude can connect to external systems using MCP.

Typical integrations include:

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

# Roadmap

Planned improvements:

- stack-specific presets
- enhanced QA automation
- architecture validation
- deeper MCP integrations
- deployment pipeline templates

---

# Contributing

Contributions are welcome.

Please ensure:

- architecture rules are respected
- tests are included or updated
- security guidelines are followed
- changes remain small and focused

---

# Need Help Implementing This?

I help teams implement **agentic development workflows using Claude Code**.

Services include:

- Claude Code workflow setup
- AI development workflow audits
- agentic SDLC consulting

Contact: (add your email or website)

---

# License

MIT