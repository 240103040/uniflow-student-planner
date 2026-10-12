# AI-native development process

## Source of truth
After tasks have been transferred to GitHub, GitHub Issues are the canonical active backlog. `_docs/github-issues/` contains issue-body drafts for creating that backlog; it is not a replacement for live issues.

## Lifecycle
1. Orchestrator selects one open issue.
2. PM reads the issue and relevant docs, then rewrites it using `_docs/task-template.md`.
3. Human reviews the groomed issue before implementation.
4. Engineer implements only that issue, adds tests, and commits.
5. Engineer leaves the issue open and comments with a summary and actual test output.
6. QA independently checks every acceptance criterion against running behaviour and executes tests.
7. QA comments with `## QA: PASS` or `## QA: FAIL`, listing every criterion and test command/result.
8. If FAIL, Engineer fixes the issue without changing criteria silently; QA retests.
9. Orchestrator closes the issue only after PASS.
10. Repeat until the backlog is empty.

## Roles
- PM — grooms an issue before implementation; follows `_docs/team/pm.md`.
- Engineer — implements one groomed task; follows `_docs/team/software-engineer.md`.
- QA — independently verifies acceptance criteria; follows `_docs/team/qa-engineer.md`.

## Loop stop condition
Stop when every in-scope GitHub Issue is closed after a recorded QA PASS, all tests pass, and documentation matches the implemented behaviour. If credentials, deadlines, or external services block work, report the blocker rather than fabricating completion.

## Graph
`Open issue -> PM groom -> Engineer implement + tests -> QA verdict`
`QA FAIL -> Engineer fix -> QA retest`
`QA PASS -> Orchestrator closes issue -> next open issue`

## Git and traceability
- Commit after meaningful changes.
- Use descriptive commit messages.
- Do not fabricate GitHub issue IDs, comments, timestamps, test outputs, or QA verdicts.
- Issue opening and closing dates must be genuine and comply with the course deadline.
