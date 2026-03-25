# Frontend Rules

- Prefer React function components unless the project already uses another pattern.
- Keep presentation separate from business logic.
- Prefer local state unless state must be shared.
- Reuse existing UI primitives before introducing new component patterns.
- Preserve accessibility: labels, semantics, keyboard support, focus behavior.
- Update component or interaction tests for changed behavior.
- Use the Playwright MCP server (`playwright` tool) for browser automation, end-to-end testing, and verifying UI behavior in a real browser. Prefer it over manual verification for interaction flows.
- Avoid large prop chains when composition is clearer.