---
name: incident-triage
description: Triage a production issue across app, infra, and dependencies
---

# Workflow

1. define observed symptom
2. estimate blast radius
3. identify likely layer:
   - frontend
   - backend
   - database
   - infra
   - external dependency
4. collect evidence
5. propose top hypotheses
6. recommend containment
7. recommend next diagnostic step

## Output

- severity
- symptom
- likely layer
- top hypotheses
- containment
- next step
- owner suggestion