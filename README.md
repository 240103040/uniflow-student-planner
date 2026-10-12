# UniFlow — Student Assignment Planner

UniFlow is a simple web app that helps university students track assignments, subjects, deadlines, and completion status.

## MVP features
- Create assignments with a title, subject, and due date.
- View assignments in a dashboard.
- Mark assignments complete or pending.
- Filter by All, Pending, and Completed.
- Sort by due date.
- Persist assignments in SQLite.
- Validate required fields and show helpful errors.

## Technology
- Python 3.11+
- Django 5.2
- SQLite
- pytest + pytest-django

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
pip install -e ".[dev]"
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000

## Run tests
```bash
pytest
```

## AI-native workflow
Read `AGENTS.md` and `_docs/process.md`. GitHub Issues are the canonical backlog once created. Each issue must be groomed by PM, implemented by Engineer, and verified independently by QA. Do not close an issue until QA reports PASS.

## GitHub setup
1. Create a public repository named `uniflow-student-planner`.
2. Upload/push this project.
3. Create one GitHub Issue for each issue specification in `_docs/github-issues/`.
4. Work through each issue using the roles and lifecycle in `_docs/process.md`.
5. Record real PM/Engineer/QA activity in the issue comments. Do not fabricate timestamps or QA results.
