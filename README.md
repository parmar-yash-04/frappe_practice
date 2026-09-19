# My Practice

A focused task-management app for [Frappe Framework](https://frappeframework.com/). It provides a simple, structured way for a System Manager to plan work, assign ownership, track priorities and due dates, and manage actionable subtasks.

> This repository is a Frappe practice project and a compact example of building linked DocTypes, child tables, and client-side form behavior.

## Highlights

- Create **Practice Tasks** with a title, description, due date, and priority.
- Assign each task to a Frappe user.
- Break work into **Practice Subtasks** with `Pending`, `In Progress`, or `Done` status.
- Associate a task with any Frappe DocType through a dynamic reference.
- Submit tasks as formal records.
- Mark a task complete; its title then becomes read-only in the form.

## Data model

| DocType | Purpose | Key fields |
| --- | --- | --- |
| `Practice Task` | The submitted parent record for work to be tracked. | Task Title, Description, Due Date, Priority, Completed, Assigned To, Reference |
| `Practice Subtask` | A child-table row that represents a unit of work within a task. | Subtask Title, Status |

`Practice Task` is available to users with the **System Manager** role. `Practice Subtask` records are maintained from the task form.

## Prerequisites

- A working [Frappe Bench](https://github.com/frappe/bench) environment.
- A Frappe site on which you can install apps.

## Installation

From the root of your Bench directory:

```bash
bench get-app https://github.com/parmar-yash-04/frappe_practice.git --branch develop
bench --site <your-site> install-app my_practice
```

If the app is already installed and you pull new changes, run:

```bash
cd apps/my_practice
git pull origin develop
cd ../..
bench --site <your-site> migrate
```

Replace `<your-site>` with your site name, for example `site1.localhost`.

## Using the app

1. Sign in to your Frappe site as a user with the **System Manager** role.
2. Open **Practice Task** from the Desk search.
3. Create a task, add its priority, due date, assignee, and optional linked record.
4. Add rows to **Subtasks** and set each status as work progresses.
5. Save and submit the task.
6. Select **Completed** when the work is finished. The form makes the task title read-only to preserve its identity.

## Development

Install development hooks from the app directory:

```bash
cd apps/my_practice
pre-commit install
```

Run the app test suite from your Bench directory:

```bash
bench --site <your-site> set-config allow_tests true
bench --site <your-site> run-tests --app my_practice
```

The pre-commit configuration checks Python formatting and imports with Ruff, JavaScript formatting with Prettier, JavaScript linting with ESLint, and common repository issues.

## Continuous integration

GitHub Actions runs the server test workflow on pushes to `develop` and on pull requests. Pull requests also run pre-commit checks, Frappe Semgrep rules, and a dependency vulnerability scan with `pip-audit`.

## Contributing

1. Create a branch from `develop`.
2. Make a focused change and run the relevant tests.
3. Ensure `pre-commit` passes.
4. Open a pull request with a concise description and verification notes.

## Security

Never commit site configuration, credentials, private uploads, database dumps, logs, or local environment files. The repository's `.gitignore` is configured to exclude these local and sensitive artifacts.

## License

This project is licensed under the [MIT License](license.txt).
