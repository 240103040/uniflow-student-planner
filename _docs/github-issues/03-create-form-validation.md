# Create assignment form with validation

## Goal
Allow students to submit assignments and receive clear errors for invalid required fields.

## Acceptance criteria
- [ ] Form includes title, subject, and due date.
- [ ] A valid POST creates exactly one Assignment record.
- [ ] Missing title, subject, or due date does not create a record.
- [ ] Validation errors are visible beside the relevant field.
- [ ] Title and subject limits match the model.
- [ ] POST form includes CSRF protection.
- [ ] Automated tests cover valid and invalid submissions.

## Out of scope
- Login, file uploads, notifications, or AI features.

## Constraints
- Use Django ModelForm/server-side validation.
- Follow `_docs/design-system.md` and `_docs/testing-guidelines.md`.
