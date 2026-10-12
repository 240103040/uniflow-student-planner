# UniFlow — Product Specification

## 1. Product summary
UniFlow is a small web application for university students to organize assignments in one place. The MVP focuses on a reliable assignment list, deadlines, completion status, and simple filtering.

## 2. Problem
Students may track coursework in separate chats, notes, calendars, and learning platforms. This makes it easy to overlook an assignment or lose track of what remains unfinished.

## 3. Target users
Primary users are university students who need a lightweight personal assignment tracker. The MVP does not require accounts or collaboration.

## 4. User stories
- As a student, I can create an assignment with a title, subject, and due date.
- As a student, I can see all saved assignments in one dashboard.
- As a student, I can mark an assignment complete or pending.
- As a student, I can filter assignments by completion status.
- As a student, I can sort assignments by deadline.
- As a student, I can reload the page and still see saved assignments.
- As a student, I receive a clear validation message when input is invalid.

## 5. MVP scope
### Included
- Server-rendered Django web app.
- SQLite persistence.
- Create assignment form.
- Assignment list/dashboard.
- Required-field validation.
- Complete/pending toggle.
- All/Pending/Completed filters.
- Sort by due date, earliest first.
- Automated tests for main behaviour and edge cases.
- Setup and test instructions in README.

### Out of scope
- AI study assistant or AI-generated schedules.
- User accounts, authentication, or password recovery.
- Shared assignments or group collaboration.
- Email, push, or calendar notifications.
- File attachments.
- Mobile native app.
- Cloud deployment, analytics, and payments.

## 6. Assignment data
Each assignment has:
- `id`: database-generated primary key.
- `title`: required string, maximum 160 characters.
- `subject`: required string, maximum 100 characters.
- `due_date`: required date.
- `is_completed`: boolean, defaults to false.
- `created_at`: timestamp generated automatically.

## 7. Main interaction
1. User opens the dashboard.
2. The page shows saved assignments and a create form.
3. User enters title, subject, and due date and submits.
4. Valid input is saved to SQLite and displayed in the list.
5. Invalid input is rejected with a visible field error.
6. User may mark an assignment complete/pending or filter the list.
7. Assignment records remain after page refresh and server restart.

## 8. Functional requirements
- FR1: A visitor can view the assignment dashboard.
- FR2: A visitor can create an assignment with valid required fields.
- FR3: Empty or invalid fields do not create an assignment.
- FR4: Assignments persist in SQLite.
- FR5: A user can toggle completion status.
- FR6: A user can filter by all, pending, or completed.
- FR7: A user can sort by due date ascending.
- FR8: Forms use Django CSRF protection.
- FR9: Invalid or unknown filter values safely fall back to All.

## 9. Non-functional requirements
- The app must run locally with documented commands.
- The interface should be usable on desktop and mobile-width screens.
- User input must be validated server-side.
- The app must not require external services or API keys.
- Tests must be repeatable and must not depend on network access.

## 10. Acceptance criteria for the MVP
- The app starts after following README instructions.
- `python manage.py check` succeeds.
- `pytest` passes.
- Valid assignments can be created and persist in the database.
- Invalid submissions show errors and do not create records.
- Completion toggle works.
- Filters show only the expected assignments.
- Sorting puts earlier deadlines before later deadlines.
- README explains setup, migration, running, and tests.

## 11. Technical decisions
Initial proposal: Python 3.11+, Django 5.2, SQLite, pytest, pytest-django. This is suitable for a small server-rendered CRUD app and keeps setup simple. The stack decision should be reviewed before implementation.

## 12. Open questions / assumptions
- No login is required for the coursework MVP.
- Dates are entered as ISO date values through a browser date input.
- The first version is single-user/local; deployment and multi-user privacy are out of scope.
