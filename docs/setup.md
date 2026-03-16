# Setup Guide

## 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

## 2. Clone this repository into your project

```bash
git clone https://github.com/natrisc/claude-code-agents
```

Or copy the `.claude/` and `memory-bank/` folders into an existing project.

## 3. Make hooks executable

```bash
chmod +x .claude/hooks/*.sh
```

## 4. Start Claude

```bash
claude
```

## 5. Fill in the project context

Open `memory-bank/context/project_context.md` and complete the template.
Set its status to `accepted` in `memory-bank/state/artifact_registry.yaml`.
This opens the first gate.

## 6. Start your first sprint

Ask Claude to initialise sprint-01. The Scrum Master will copy the sprint template, set the current sprint in `workflow_state.yaml`, and begin routing work.
