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

## Default delivery flow

1. Clarify the requirement
2. Refine the backlog item or bug
3. Define acceptance criteria
4. Assess architecture impact
5. Implement the smallest correct change
6. Add or update tests
7. Review security impact
8. Review release and operational impact
9. Summarize changes, risks, and follow-up items

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