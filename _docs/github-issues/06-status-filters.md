# Filter assignments by status

## Goal
Let students show all assignments, only pending assignments, or only completed assignments.

## Acceptance criteria
- [ ] `?status=all` shows all records.
- [ ] `?status=pending` shows only incomplete records.
- [ ] `?status=completed` shows only completed records.
- [ ] Unknown status values safely fall back to All.
- [ ] Current filter is visually identifiable and accessible.
- [ ] Empty filtered results show a helpful message.
- [ ] Tests cover all filters and an unknown filter.

## Out of scope
- Search by keyword or subject.

## Constraints
- Follow `_docs/design-system.md` and `_docs/api.md`.
