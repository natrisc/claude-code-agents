# Coding Standards

Fill in the sections below for your project. Agents reference this file instead of
regenerating conventions each session.

---

## Language and stack

<!-- e.g. TypeScript 5, Node 20, React 18, Python 3.12, Rust 1.78 -->

## Naming conventions

<!-- e.g. camelCase for variables, PascalCase for types, snake_case for DB columns -->

## File and folder structure

<!-- e.g. feature-based folders, colocated tests, shared/ for cross-package code -->

## Types

<!-- e.g. prefer branded types for IDs, use `type` over `interface` unless merging -->

## Functions

- prefer small, composable, pure functions
- no function longer than 40 lines without strong justification
- no class where a function suffices
- extract helpers only when reused or required for testability

## Error handling

<!-- e.g. Result types, thrown errors, structured logging format -->

## Testing

- unit tests colocated with source: `*.spec.ts`
- integration tests in `tests/`
- prefer strong assertions (`toEqual`) over weak ones (`toBeDefined`)
- test edge cases and boundaries, not just the happy path
- do not test what the type checker already enforces

## Imports

<!-- e.g. use `import type` for type-only imports -->

## Comments

- no comments except for critical caveats
- prefer self-explanatory names over explanatory comments

## Formatting

<!-- e.g. prettier, ruff, rustfmt — command to run -->

## Linting

<!-- e.g. ESLint rules, ruff rules, clippy — command to run -->
