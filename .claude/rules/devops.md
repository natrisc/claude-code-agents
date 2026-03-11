# DevOps Rules

- Prefer reversible changes.
- Document migration and rollback implications.
- Preserve CI stability.
- Call out infra drift or environment-specific assumptions.
- For deploy-affecting changes, mention rollout, rollback, and monitoring expectations.
- Do not modify production infrastructure paths without explicit approval.
- Prefer observable systems: logs, metrics, tracing, health checks.