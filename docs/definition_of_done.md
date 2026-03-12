# Definition of Done

A task is complete only when all of the following are true.

## Code

- [ ] implements only the committed sprint scope
- [ ] follows patterns in `docs/architecture_overview.md`
- [ ] follows rules in `docs/coding_standards.md`
- [ ] no secrets, tokens, or credentials in code or logs
- [ ] handlers are thin — business rules in services/modules

## Tests

- [ ] unit tests cover new logic and edge cases
- [ ] integration tests cover new API behaviour
- [ ] all existing tests still pass
- [ ] no tests skipped without documented reason

## Review

- [ ] code review comments addressed
- [ ] no TODO left without a linked backlog item
- [ ] security check complete — see `docs/security_baseline.md`

## Delivery

- [ ] rollback path documented
- [ ] deployment impact assessed
- [ ] monitoring impact assessed

## Artifacts

- [ ] sprint delivery artifact updated
- [ ] acceptance criteria checked pass/fail
- [ ] QA sign-off recorded
- [ ] security sign-off recorded
