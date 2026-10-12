# Agent instructions

## Project
UniFlow is a student assignment planner. Follow `_docs/plan.md`; do not silently expand scope.

## Commands
- `python -m pip install -e ".[dev]"` — install dependencies
- `python manage.py migrate` — apply migrations
- `python manage.py runserver` — start development server
- `pytest` — run the test suite
- `python manage.py check` — Django system check

## Documents
- `_docs/plan.md` — product specification
- `_docs/process.md` — AI-native issue workflow and roles
- `_docs/task-template.md` — issue grooming template
- `_docs/testing-guidelines.md` — testing policy
- `_docs/design-system.md` — UI rules
- `_docs/api.md` — models and routes
- `_docs/team/pm.md` — PM role
- `_docs/team/software-engineer.md` — Engineer role
- `_docs/team/qa-engineer.md` — QA role
- `_docs/github-issues/` — proposed issue bodies to create on GitHub
- `_docs/chat-brainstorm.md` — brainstorm record

## Rules
- Work on one GitHub Issue at a time.
- Read the full issue and its acceptance criteria before implementation.
- PM grooms the issue before Engineer starts.
- Engineer must not change acceptance criteria or close issues.
- Engineer writes tests and commits changes; leave the issue open.
- QA independently checks every acceptance criterion and reports PASS or FAIL.
- QA does not fix implementation code.
- If QA reports FAIL, Engineer fixes the problem and QA retests.
- The orchestrator closes the issue only after QA reports PASS.
- Add dependencies only after reviewing `pyproject.toml` and explaining why.
- Keep changes within the scope of the issue.
- Never claim tests passed unless you ran them and observed the result.
