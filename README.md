# Employee Management System (Django)

A beginner-friendly Django CRUD project matching the supplied machine-test requirements.

## Features
- Employee model: name, unique email, department, salary, joining date
- Add employee
- Dashboard listing and total employee count
- Search/filter by employee name or department using `request.GET`
- Delete employee (POST form with CSRF protection)
- Edit employee salary or department (the form allows editing all fields)

## Setup (Windows / VS Code)

Open a terminal in the folder containing `manage.py`:

```cmd
python -m venv env
env\Scripts\activate
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Notes
- SQLite is configured by default, so no separate database installation is required.
- The `department` search matches part of a department name; the `name` search matches part of an employee name. Search is case-insensitive.
- To use a department-only search, remove the `Q(name__icontains=search)` condition in `app/views.py`.
