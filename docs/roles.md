# AI Scrum Team Roles

| Role | Owns | Reads |
| --- | --- | --- |
| Product Owner | `context/*`, `sprints/{sprint}/po_decision.md` | everything |
| Product Manager | `planning/roadmap.md`, `epics.md`, `backlog.md` | context |
| Scrum Master | `sprints/{sprint}/intent.md`, `state/*`, `tasks/*` | everything |
| Business Analyst | `analysis/*` | context, planning |
| System Architect | `architecture/*` | context, analysis |
| Frontend Developer | `sprints/{sprint}/delivery/frontend.md` | context, analysis, architecture |
| Backend Developer | `sprints/{sprint}/delivery/backend.md` | context, analysis, architecture |
| DevOps Engineer | `sprints/{sprint}/delivery/devops.md` | architecture, delivery |
| QA Tester | `sprints/{sprint}/quality/test_*.md` | analysis, delivery |
| Security Officer | `sprints/{sprint}/quality/security_review.md` | architecture, analysis, quality |

Role boundaries are strict. No agent edits artifacts owned by another role.

## When to Involve Each Specialist

- **Product Owner** — acceptance criteria, story scope, release acceptance
- **Product Manager** — priority, trade-offs, roadmap fit
- **Business Analyst** — process clarification, domain rules, dependencies
- **System Architect** — cross-cutting design, new modules, API or event contract changes, architectural trade-offs
- **Front-End Developer** — UI, UX, React, accessibility, client logic
- **Back-End Developer** — API, services, Python, Rust, persistence, integrations
- **QA Tester** — regression, edge cases, test strategy, reproducibility
- **Security Officer** — auth, permissions, secrets, validation, exposure, dependencies
- **DevOps Engineer** — CI/CD, infra, containers, observability, migrations, rollout and rollback
