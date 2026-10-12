# Add Assignment model and database migration

## Goal
Persist assignment records in SQLite using the fields specified in `_docs/plan.md`.

## Acceptance criteria
- [ ] Assignment has title (max 160), subject (max 100), due date, completion boolean defaulting false, and created timestamp.
- [ ] A migration creates the table.
- [ ] Applying migrations succeeds on a clean database.
- [ ] Model string representation is useful for debugging/admin.
- [ ] Automated tests verify defaults and stored field values.

## Out of scope
- Dashboard form and UI (follow-up issue #3/#4).

## Constraints
- Follow `_docs/api.md` and `_docs/testing-guidelines.md`.
- Do not add user accounts or external database services.
