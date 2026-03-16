# Core Concepts

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

## The Solution

This repository implements a **repository-centric AI Scrum team** for Claude Code.

Instead of relying on conversation context, agents communicate through **canonical documents** in the repository. Each agent reads its required input artifacts, writes to its owned output artifacts, and the system enforces gate-based progression before any work proceeds.

The product evolves across multiple sprints against one active product baseline — with formal change control, escalation handling, a full event log, and a live sprint dashboard.

## Supported Stacks

Engineering rules in `.claude/rules/` cover:

- TypeScript / Node
- React
- Python
- Rust
- REST APIs
- cloud-native and containerised systems

The system is stack-agnostic — rules are additive, not prescriptive.
