# Data model and routes

## Model: Assignment
- `id`: integer primary key
- `title`: required string, max 160
- `subject`: required string, max 100
- `due_date`: required date
- `is_completed`: boolean, default false
- `created_at`: creation timestamp

## Routes
- `GET /` — dashboard; optional `status=all|pending|completed`; optional `sort=due_date`.
- `POST /` — create assignment; invalid input re-renders the form with errors.
- `POST /assignments/<id>/toggle/` — toggle completion state and redirect to dashboard.

All state-changing actions use POST and Django CSRF protection. The MVP has no public JSON API.
