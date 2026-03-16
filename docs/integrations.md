# MCP Integrations

Connect Claude to external systems via `.mcp.json`:

| Integration | Purpose |
| --- | --- |
| GitHub | issues, PRs, code search |
| Linear or Jira | backlog management |
| Postgres | live database queries |
| Notion or Confluence | documentation |
| Sentry | error tracking |
| Kubernetes | cluster observability |

## Configuration

Edit `.mcp.json` at the repository root to enable integrations. Claude will automatically pick up configured MCP servers when started.
