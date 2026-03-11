# Personal Claude Code Preferences

## Working Style

- Prefer maintainability, safety, and developer velocity.
- For complex work, draft an approach before coding.
- If there are multiple reasonable approaches, briefly compare trade-offs.
- Prefer small, composable, testable functions.
- Prefer clarity over cleverness.
- Avoid introducing classes when small testable functions are sufficient.
- Avoid adding comments except for critical caveats; prefer self-explanatory code.
- Avoid extracting helper functions unless there is a compelling reason:
  - the logic is reused
  - extraction is necessary for meaningful unit testing
  - it significantly improves readability

## TDD

- Follow TDD by default:
  1. scaffold stub
  2. write a failing test
  3. implement
  4. refactor only after tests pass

## Function Design Preferences

- Use existing domain vocabulary when naming functions and types.
- Prefer simple, composable, testable functions.
- Prefer explicit inputs over hidden dependencies.
- Remove unused parameters.
- Avoid unnecessary type casts when they can be moved to function boundaries.

## Test Design Preferences

- Prefer tests that can fail for real defects.
- Prefer strong assertions over weak assertions.
- Prefer comparing whole structures in one assertion when practical.
- Prefer integration tests over heavy mocking when that gives more confidence.
- Test edge cases, realistic inputs, unexpected inputs, and boundaries.
- Avoid testing conditions already guaranteed by the type checker.
- Prefer invariants and properties over one-off hardcoded examples when practical.
- Use `expect.any(...)` for values that are intentionally variable.

## Self-Review Checklist for Functions

When evaluating a function, check:

1. Is it easy to follow?
2. Is complexity unnecessarily high?
3. Would a clearer data structure or algorithm help?
4. Are any parameters unused?
5. Are any casts unnecessary?
6. Is it testable without awkward mocking?
7. Are there hidden dependencies that should become arguments?
8. Are there better names consistent with the codebase?

## Self-Review Checklist for Tests

When evaluating a test, check:

1. Are inputs explained and intentional?
2. Can the test fail for a real defect?
3. Does the description match the assertion?
4. Is the expected value independent from the implementation?
5. Does the test follow the same quality standards as production code?
6. Could invariants or properties express intent better?
7. Are assertions strong and specific?
8. Are edge cases and boundaries covered appropriately?

## Personal Shortcuts

### QNEW
Understand and apply all best practices in this CLAUDE.md.

### QPLAN
Analyze similar parts of the codebase and ensure the plan:
- is consistent with the codebase
- introduces minimal change
- reuses existing code

### QCODE
Implement the plan, run relevant tests, and run formatting/lint/typecheck commands appropriate to the repository.

### QCHECK
Act as a skeptical senior engineer and review major changes against:
- function quality
- test quality
- implementation quality

### QCHECKF
Act as a skeptical senior engineer and review major edited or added functions.

### QCHECKT
Act as a skeptical senior engineer and review major edited or added tests.

### QUX
Act as a human UX tester and list the highest-priority scenarios to test.