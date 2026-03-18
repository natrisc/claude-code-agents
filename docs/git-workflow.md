# Git Workflow

This repository follows a **human-supervised AI delivery workflow**.

Claude helps plan, implement, review, and validate changes.
A human developer remains responsible for final approval and merging.

## Who Makes Code Changes?

Claude can:

- analyze requirements
- propose a plan
- implement code changes
- add or update tests
- review code quality
- review test quality
- suggest a commit message

A human developer is responsible for:

- deciding when work is ready
- reviewing the final diff
- approving commits and pushes
- opening and merging pull requests

## Who Commits?

Default model:

- Claude prepares the change
- Claude may suggest a Conventional Commit message
- the human developer decides whether to commit
- the human developer decides whether to push

If you explicitly use the `QGIT` shortcut, Claude may:

1. stage changes
2. create a commit
3. push the branch

That workflow should be treated as **opt-in**, not automatic.

## Branch Strategy

Use **short-lived feature branches**.

Recommended naming:

- `feat/<short-description>`
- `fix/<short-description>`
- `refactor/<short-description>`
- `chore/<short-description>`

Examples:

```bash
git checkout -b feat/linkedin-publishing
git checkout -b fix/instagram-timeout
git checkout -b refactor/publisher-abstraction
```

## Default Change Flow

```text
Create branch
→ plan
→ implement
→ review diff
→ commit
→ push
→ PR
→ merge
```

## Pull Request Workflow

Each meaningful change should go through a pull request.

A good PR should include:

- what changed
- why it changed
- affected areas
- tests run
- known risks
- rollout or migration notes if relevant

Claude can help draft this summary.

## Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

Examples:

```text
feat(api): add linkedin publishing endpoint
fix(web): handle expired auth token redirect
refactor(shared): simplify social media validation
test(api): add publish failure integration coverage
```

Do not mention Claude or Anthropic in commit messages.

## Merge Strategy

Prefer:

- small pull requests
- one logical change per PR
- squash merge for cleanup when appropriate

Avoid:

- long-running branches
- mixing unrelated refactors with feature work
- direct commits to main

## Protected Branch Recommendation

Protect `main` with:

- required PR review
- required status checks
- no force push
- no direct push

Recommended required checks: tests, lint, typecheck, any security or build checks used by the project.

## Release Flow

For release-sensitive changes:

1. complete implementation
2. review diff and test output
3. confirm rollback notes
4. merge via PR
5. deploy through normal CI/CD pipeline

## Recommended Ownership Model

The cleanest model for teams is:

- Claude owns implementation assistance
- the engineer owns repository history
- the team owns merge and release decisions

This keeps AI fast, while keeping git history and production responsibility under human control.
