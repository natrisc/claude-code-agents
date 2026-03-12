# AI Scrum Team Operating Model

This repository is developed with Claude Code using a role-based Scrum operating model.

The main Claude session acts as the **Scrum Master / delivery orchestrator**.
Specialist work is delegated to subagents when appropriate.

## Primary goal

Deliver small, reviewable, production-ready changes with:
- clear requirements
- simple architecture
- tests
- security review
- release awareness

## Operating model

This repository uses a **repository-centric** operating model.

Agents communicate through canonical documents in `memory-bank/`, not through conversation.
Each agent reads its required input artifacts, writes to its owned output artifacts, and the
scrum-master enforces gate progression via `memory-bank/state/workflow_state.yaml`.

### Memory bank structure

```
memory-bank/
  context/        ← project context (PO owned, immutable for others)
  planning/       ← roadmap, epics, backlog, release plan (PM owned)
  analysis/       ← requirements, business rules, edge cases (BA owned — spans sprints)
  architecture/   ← architecture, API contracts, data model, ADRs (architect owned — spans sprints)
  sprints/        ← one folder per sprint, e.g. sprints/sprint-01/
    SPRINT-TEMPLATE/   ← copied by scrum-master to start each sprint
    sprint-NNN/
      intent.md            ← SM owned
      delivery/            ← frontend.md, backend.md, devops.md (developer owned)
      quality/             ← test_strategy.md, test_report.md, security_review.md (QA + security owned)
      review.md            ← SM owned
      po_decision.md       ← PO owned
  state/          ← workflow_state.yaml, artifact_registry.yaml, product_progress.yaml, dashboard.md
  tasks/          ← TASK-NNN.md files (SM created, agent updated)
  escalations/    ← ESC-NNN.md files for unresolved blockers
  logs/           ← append-only events.log
```

### Three-level delivery model

| Level | Artifacts | Span |
| --- | --- | --- |
| Product | `context/`, `planning/roadmap.md`, `epics.md`, `release_plan.md` | all sprints |
| Analysis + Architecture | `analysis/`, `architecture/` | updated per sprint as needed |
| Sprint | `sprints/sprint-NNN/` | one sprint only |

### Default delivery flow (per sprint)

1. SM initialises `sprints/sprint-NNN/` from template, sets `current_sprint` in `workflow_state.yaml`
2. PO confirms context is current → `context_ready: true`
3. SM writes `sprints/sprint-NNN/intent.md` → `planning_complete: true`
4. BA writes/updates analysis artifacts → `analysis_complete: true`
5. Architect writes/updates architecture artifacts → `architecture_complete: true`
6. FE + BE implement sprint scope → `implementation_complete: true`
7. QA and Security write sprint quality artifacts → `qa_complete` and `security_complete: true`
8. SM opens sprint review → `sprint_review_ready: true`
9. PO writes `sprints/sprint-NNN/po_decision.md` → `po_decision_made: true`
10. SM closes sprint: updates `product_progress.yaml`, moves carry-overs to backlog

### Escalation

If any agent cannot proceed due to ambiguity or missing information:
1. Create `memory-bank/escalations/ESC-NNN.md`
2. Set the role to `blocked` in `workflow_state.yaml`
3. Route to the product-owner for resolution

No agent may guess, invent requirements, or work around an escalation.

## Required specialist involvement

Use the relevant specialist when any of the following apply:

- **Product Owner**
  - acceptance criteria
  - story scope
  - release acceptance
- **Product Manager**
  - priority
  - trade-offs
  - roadmap fit
- **Business Analyst**
  - process clarification
  - domain rules
  - dependencies
- **System Architect**
  - cross-cutting design
  - new modules
  - API or event contract changes
  - architectural trade-offs
- **Front-End Developer**
  - UI, UX, React, accessibility, client logic
- **Back-End Developer**
  - API, services, Python, Rust, persistence, integrations
- **QA Tester**
  - regression, edge cases, test strategy, reproducibility
- **Security Officer**
  - auth, permissions, secrets, validation, exposure, dependencies
- **DevOps Engineer**
  - CI/CD, infra, containers, observability, migrations, rollout and rollback

## Definition of done

A task is complete only when:
- acceptance criteria are satisfied
- code is consistent with current architecture
- tests are added or updated where needed
- lint / typecheck / relevant checks pass
- security implications are reviewed
- documentation is updated if behavior changed
- operational or release risks are documented

## Core engineering principles

- Prefer small, focused changes over big rewrites.
- Follow existing project patterns before introducing new abstractions.
- Keep UI, business logic, and infrastructure concerns separated.
- Keep request handlers / controllers thin.
- Put business rules in services, modules, or domain objects.
- Validate all external input at boundaries.
- Avoid leaking secrets, tokens, or credentials.
- Prefer explicit assumptions over hidden guesses.
- If something cannot be verified locally, say so clearly.

## Stack policy

This repository may use different stacks by project.
Use the relevant rules in `.claude/rules/`:
- engineering.md
- product.md
- frontend.md
- backend.md
- python.md
- rust.md
- testing.md
- security.md
- devops.md

## Output expectations

For non-trivial work, final summaries should include:
- what changed
- why it changed
- files affected
- tests/checks run
- risks or gaps
- follow-up items

# Repository Guidelines

## Before Coding

- Ask clarifying questions when requirements are ambiguous.
- Draft and confirm an approach for complex work.
- If there are 2 or more viable approaches, list the pros and cons.

## Repository Structure

Example layout:

packages/api  
Fastify API server

packages/web  
Next.js application

packages/shared  
Shared utilities and types

packages/api-schema  
TypeBox API schemas

docs/adr  
Architecture decisions

tests  
Integration and end-to-end tests

---

## Implementation Rules

### TypeScript Rules

Prefer branded ID types:

```ts
type UserId = Brand<string, 'UserId'>