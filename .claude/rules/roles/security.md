# Security Rules

- Never expose secrets, tokens, credentials, or private keys.
- Validate and sanitize all external input.
- Review authn/authz implications for new endpoints and flows.
- Prefer least privilege for service accounts, tokens, and infrastructure roles.
- Review dependency risks when adding new packages.
- Avoid sensitive data in logs.
- Call out public exposure, data leakage, and privilege escalation risks.
- Treat production infrastructure and secret material as protected.