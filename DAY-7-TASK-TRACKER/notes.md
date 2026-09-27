# Day 7 – Mini Project: Task Tracker Backend API

## Intern ID
C.ID: ZST/2026/DRM/KOP-0009

## Project Title
Task Tracker Backend API

## Objective
To develop a Django-based Task Tracker Backend API that allows users to create, retrieve, update, and delete tasks.

## Technologies Used
- Python
- Django
- SQLite
- JSON
- Postman
- React

## Project Structure

DAY-7-TASK-TRACKER
│
├── backend
│   └── tasktracker
│       ├── manage.py
│       ├── db.sqlite3
│       ├── tasktracker
│       │   ├── settings.py
│       │   └── urls.py
│       │
│       └── tasks
│           ├── models.py
│           ├── views.py
│           ├── urls.py
│           └── migrations
│
└── notes.md

## Task Model

The Task model contains the following fields:

1. Task Name
2. Description
3. Status
4. Created Date

## CRUD API Endpoints

### 1. GET – Retrieve All Tasks

Endpoint:

GET /api/tasks/

URL:

http://127.0.0.1:8000/api/tasks/

This API retrieves all tasks stored in the database.

### 2. POST – Add New Task

Endpoint:

POST /api/tasks/

URL:

http://127.0.0.1:8000/api/tasks/

Example JSON:

{
    "task_name": "Learn Django",
    "description": "Complete Django Task Tracker API",
    "status": "Pending"
}

This API creates and stores a new task in the database.

### 3. PUT – Update Task

Endpoint:

PUT /api/tasks/<task_id>/

Example:

http://127.0.0.1:8000/api/tasks/1/

This API updates an existing task.

### 4. DELETE – Delete Task

Endpoint:

DELETE /api/tasks/<task_id>/

Example:

http://127.0.0.1:8000/api/tasks/1/

This API deletes an existing task.

## Database

SQLite database is used to store task information.

Migration commands used:

python manage.py makemigrations

python manage.py migrate

## API Testing

Postman is used to test the APIs.

The following API operations are tested:

- GET – Retrieve all tasks
- POST – Create a new task
- PUT – Update a task
- DELETE – Delete a task

## GET API Testing

The GET API was tested using:

http://127.0.0.1:8000/api/tasks/

Initial response:

{
    "status": "success",
    "tasks": []
}

This confirmed that the GET API was successfully connected to the database.

## Django Server

The Django development server was started using:

python manage.py runserver

Server URL:

http://127.0.0.1:8000/

The server started successfully without any system errors.

## Learning Outcomes

During this project, I learned:

- How to create a Django project.
- How to create a Django application.
- How to create Django models.
- How to perform database migrations.
- How to use SQLite database.
- How to create CRUD API endpoints.
- How to handle GET, POST, PUT and DELETE requests.
- How to return JSON responses.
- How to test APIs using Postman.
- Basic React and Django API integration.

## Conclusion

The Task Tracker Backend API was developed using Django. The project demonstrates CRUD operations, database integration, JSON responses, and API testing. The backend can be connected with a React frontend using fetch() to create a complete full-stack Task Tracker application.