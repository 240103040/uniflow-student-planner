# Toggle assignment completion

## Goal
Allow a student to switch an assignment between Pending and Completed.

## Acceptance criteria
- [ ] Each assignment has a status action.
- [ ] A POST action toggles `is_completed`.
- [ ] Action redirects back to the dashboard.
- [ ] Unknown assignment IDs return HTTP 404.
- [ ] GET requests cannot change state.
- [ ] CSRF protection remains enabled.
- [ ] Tests cover both toggling directions and unknown IDs.

## Out of scope
- Deleting assignments or editing existing assignment details.

## Constraints
- Follow `_docs/api.md` and `_docs/testing-guidelines.md`.
- Do not close the issue as Engineer.
