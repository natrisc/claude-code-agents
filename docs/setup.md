# Setup Guide

## 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

## 2. Clone this repository into your project

```bash
git clone https://github.com/natrisc/claude-code-agents
```

Or copy the `.claude/`, `memory-bank/`, and `workflow/` folders into an existing project.

## 3. Install Python dependencies

The enforcement layer requires PyYAML:

```bash
pip install pyyaml
```

## 4. Make hooks and scripts executable

```bash
chmod +x .claude/hooks/*.sh
chmod +x workflow/scripts/*.py
```

## 5. Verify the enforcement layer

```bash
python workflow/scripts/validate_gate.py --all
```

All gates will show `[FAIL]` except `context_ready`, which will show `[PASS]` once you complete step 7 below. This is expected.

## 6. Start Claude

```bash
claude
```

## 7. Activate the project

Ask Claude to start your project. The Scrum Master will route an `activate-project` task to the Product Owner, who will create `memory-bank/context/project_context.md` from your input.

Once the PO completes the task, set its status to `accepted` in `memory-bank/state/artifact_registry.yaml` and run the validator to confirm the first gate opens:

```bash
python workflow/scripts/validate_gate.py context_ready
# → [PASS] context_ready
```

## 8. Generate the initial dashboard

```bash
python workflow/scripts/regenerate_dashboard.py
```

## 9. Start your first sprint

Ask Claude to initialise sprint-01. The Scrum Master will copy the sprint template, set the current sprint in `workflow_state.yaml`, create the first task, and begin routing work.

---

## Repository structure

```
.claude/
  agents/         ← role agent definitions
  hooks/          ← pre/post tool hooks
  rules/
    shared/       ← engineering and testing rules
    roles/        ← role-specific rules
    languages/    ← language-specific rules
  skills/         ← reusable workflow skills
memory-bank/
  context/        ← project context (PO owned)
  planning/       ← roadmap, epics, backlog (PM owned)
  analysis/       ← requirements, business rules (BA owned)
  architecture/   ← architecture, API contracts (Architect owned)
  sprints/        ← one folder per sprint
  state/          ← workflow_state.yaml, artifact_registry.yaml, dashboard.md
  tasks/          ← TASK-NNN.md files
  escalations/    ← ESC-NNN.md files
  logs/           ← append-only events.log
workflow/
  contracts/      ← gates.yaml (gate artifact contracts)
  scripts/        ← validate_gate.py, validate_task.py, regenerate_dashboard.py
docs/             ← documentation
```

## Key files

| File | Purpose |
| --- | --- |
| `memory-bank/state/workflow_state.yaml` | Single source of truth for gate flags, roles, and tasks |
| `memory-bank/state/artifact_registry.yaml` | Artifact ownership and acceptance status |
| `workflow/contracts/gates.yaml` | Required files and prerequisites per gate |
| `workflow/scripts/validate_gate.py` | Gate validator — run before opening any gate |
| `workflow/scripts/validate_task.py` | Task validator — run before accepting any task |
| `workflow/scripts/regenerate_dashboard.py` | Dashboard generator — run after every state change |
| `memory-bank/state/sprint_playbook.md` | Sprint init and close procedures |
