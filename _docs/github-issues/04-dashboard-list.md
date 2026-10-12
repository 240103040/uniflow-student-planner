# Show assignment dashboard

## Goal
Show saved assignments in a clean dashboard with a helpful empty state.

## Acceptance criteria
- [ ] `GET /` returns HTTP 200.
- [ ] Saved assignments show title, subject, due date, and status.
- [ ] Empty database displays guidance to add the first assignment.
- [ ] Form validation errors remain visible after invalid submission.
- [ ] Layout remains usable at narrow viewport widths without horizontal overflow.
- [ ] Labels and controls are semantic and keyboard accessible.
- [ ] Tests verify the page and empty/list states.

## Out of scope
- Advanced charts, calendar view, or user profiles.

## Constraints
- Follow `_docs/design-system.md`.
- Use existing Django templates and CSS; no frontend framework unless approved.
