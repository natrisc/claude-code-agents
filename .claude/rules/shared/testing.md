# Testing Rules

- Use the Playwright MCP server (`playwright` tool) for end-to-end and browser-based tests. Prefer it when verifying full user flows, accessibility, or rendering behavior in a real browser.
- Test behavior, not implementation details.
- Prefer the smallest test scope that gives confidence.
- Add regression coverage for bugs.
- Cover edge cases, unhappy paths, and permission-related behavior where relevant.
- If a full test suite is too expensive, run the most relevant targeted tests and state what was not run.
- Final summaries must mention what was tested and what remains unverified.