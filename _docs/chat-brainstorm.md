# UniFlow brainstorm record

> Coursework note: this document records the project decisions and the initial discussion summary. Continue adding the real question-and-answer turns from the chat used for the assignment. Do not represent a reconstructed summary as a verbatim transcript.

## Initial idea
I want to build a student assignment planner. Help me set the scope precisely. Ask one question at a time and keep the output short.

## Discussion summary and decisions
**Problem:** Students can lose track of coursework when assignments and deadlines are spread across different tools.

**Target users:** University students who need a simple personal assignment tracker.

**Core workflow:** Open dashboard -> create assignment -> see assignment in list -> mark complete/pending -> filter and sort -> reload and see saved data.

**Required fields:** Title, subject, due date.

**Persistence:** Save assignments in SQLite.

**Platform:** Server-rendered web app.

**Technology proposal:** Python + Django + SQLite + pytest. The stack is deliberately kept simple and should be reviewed before implementation.

**MVP features:** Create/list assignments, required-field validation, status toggle, status filter, due-date sort, persistence, automated tests, README.

**Out of scope:** AI features, accounts, collaboration, notifications, file attachments, native mobile app, payments, deployment.

**Design:** Clean responsive layout with visible labels, readable errors, clear empty states, and status text.

**Testing:** Automated tests for valid creation, invalid input, listing, persistence, toggle, filters, and sorting. QA must independently report PASS/FAIL.

## Final product decision
Build UniFlow as a local-first Django web application for university assignment tracking. GitHub Issues are the canonical backlog after migration. Process each issue through PM grooming, Engineer implementation, independent QA, and close only after QA PASS.

## Prompts to preserve for the actual transcript
1. "Help me set the scope for this project precisely. Ask me one question at a time and keep your output short."
2. "Summarize the decisions we made as a product specification. Do not write code."
3. "Read `_docs/plan.md`. Propose multiple options for the tech stack and explain each. Don't write code yet."
4. "Create a backlog in `_docs/tasks.md` using the required task template. The first task must set up an empty project with a passing test. Don't write code yet."
