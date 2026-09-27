# WEEK 4 – DAY 3
# Request Handling in Django

## 1. Objective

The objective of Day 3 was to understand how Django handles different HTTP request methods.

In this task, the following HTTP methods were implemented and tested:

- GET
- POST
- PUT
- DELETE

A Django API endpoint was created to receive requests and return JSON responses.

---

## 2. Technologies Used

- Python
- Django
- Visual Studio Code
- Postman
- PowerShell
- SQLite

---

## 3. Project Structure

The Day 3 project was created separately inside the `DAY-3-REQUEST-HANDLING` folder.

```text
DAY-3-REQUEST-HANDLING
│
├── tasktracker
│   │
│   ├── manage.py
│   ├── db.sqlite3
│   │
│   ├── tasktracker
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── tasks
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
│
├── venv
│
├── day3_get.png
├── day3_post.png
├── day3_put.png
├── day3_delete.png
│
└── notes.md