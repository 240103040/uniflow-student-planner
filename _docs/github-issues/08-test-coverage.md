# Add automated tests for MVP behaviour

## Goal
Provide repeatable test coverage for the MVP's primary user flows and edge cases.

## Acceptance criteria
- [ ] Tests cover dashboard response and empty state.
- [ ] Tests cover valid assignment creation and required-field errors.
- [ ] Tests cover completion toggle and unknown IDs.
- [ ] Tests cover status filters and invalid filter fallback.
- [ ] Tests cover deadline sorting and persistence via database-backed model/view behaviour.
- [ ] `pytest` completes successfully.
- [ ] Test command and actual result are recorded in the issue comment.

## Out of scope
- Load testing, penetration testing, or external service tests.

## Constraints
- Follow `_docs/testing-guidelines.md`.
- QA role must independently run tests and not modify implementation.
