---
name: escalation-review
description: Review open escalations, determine their status, and decide how to route or resolve them
---

# Workflow

1. read all open escalations in `memory-bank/escalations/`
2. read `memory-bank/state/workflow_state.yaml` — identify which roles are blocked
3. for each escalation:
   a. classify: ambiguous requirement / missing input / contract conflict / scope change / other
   b. identify the correct resolution owner (product-owner, product-manager, system-architect, or user)
   c. determine: resolve now / route to agent / escalate to user
4. summarise open blockers and recommended actions

## Output

- open escalations table (ID, type, blocked role, resolution owner, recommended action)
- escalations requiring user input (explicit list)
- escalations that can be routed to an agent (with task type)
- delivery impact: which gates are blocked and why
