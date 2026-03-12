# API Contracts

**Owner**: system-architect
**Status**: draft
**Depends on**: architecture/architecture.md, analysis/requirements.md

---

## Endpoints

### Template

```
## <METHOD> /path/to/endpoint

**Description**: What this endpoint does
**Auth**: required / not required / token type

### Request

Headers:
- Authorization: Bearer <token>

Body:
```json
{
  "field": "type"
}
```

### Response 200

```json
{
  "field": "type"
}
```

### Error responses

| Code | Meaning |
|------|---------|
| 400 | Validation error |
| 401 | Unauthenticated |
| 403 | Forbidden |
| 404 | Not found |
| 500 | Internal error |

### Validation rules

- field: required, max 255 chars
```

---

## Backward compatibility notes

<!-- Any breaking changes and migration path -->
