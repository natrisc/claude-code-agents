# Security Baseline

Fill in the sections below for your project. The Security Officer references this file
on every sprint review.

---

## Authentication

<!-- e.g. JWT with RS256, session cookies, API keys — describe the expected pattern -->

## Authorisation

<!-- e.g. RBAC, ABAC, scope-based — describe the expected checks -->

## Input validation

- validate all external input at system boundaries
- reject unknown fields by default
- sanitise before use in SQL, shell, HTML, and file paths

## Secrets handling

- no secrets in code, environment files committed to source control, or logs
- secrets via environment variables or a secrets manager
- rotate credentials on suspected exposure

## Dependencies

- no new dependencies without checking for known CVEs
- lock files committed and up to date
- flag any package with no recent maintenance

## Data exposure

- no PII, credentials, or internal IDs in API responses unless required
- no sensitive data in logs
- no sensitive data in error messages returned to clients

## Transport

<!-- e.g. TLS 1.2+ required, HSTS, certificate pinning -->

## Audit and logging

- all authentication events logged
- all authorisation failures logged
- no sensitive values in log lines

## Known exceptions

<!-- List any accepted deviations from the above, with rationale -->
