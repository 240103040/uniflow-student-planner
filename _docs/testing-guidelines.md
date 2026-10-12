# Testing guidelines

- Use pytest and pytest-django.
- Prefer Django test client tests for views and forms.
- Test both successful and unsuccessful paths.
- Test validation at the server, not only in the browser.
- Tests must not require internet access or real user data.
- Use isolated test database state.
- For each issue, map tests to acceptance criteria.
- Run `pytest` after each implementation task and report the actual output.
- Run `python manage.py check` for project-level changes.
- QA must not edit code; it reports evidence and a PASS/FAIL verdict.
