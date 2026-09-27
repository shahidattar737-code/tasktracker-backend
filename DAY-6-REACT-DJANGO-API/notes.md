# Day 6 — Connecting React with Django API

## Internship Training — Week 4

**Training:** Python Backend & Django Fundamentals
**Day:** 6
**Topic:** Connecting React with Django API
**Intern Name:** Shahid Attar
**Intern ID:** C.ID: ZST/2026/DRM/KOP-0009

---

## 1. Objective

The objective of Day 6 is to connect a React frontend application with a Django backend API.

React is used to create the frontend user interface, while Django provides the backend API and sends data in JSON format.

The React application uses the `fetch()` function to request data from the Django API.

---

## 2. Concepts Learned

During Day 6, the following concepts were practiced:

* React frontend
* Django backend
* REST API
* JSON data
* API endpoint
* `fetch()` function
* `useEffect()` hook
* `useState()` hook
* GET request
* Connecting frontend with backend
* CORS configuration

---

## 3. Project Structure

The Day 6 project contains separate frontend and backend folders.

```text
DAY-6-REACT-DJANGO-API
│
├── backend
│   │
│   ├── venv
│   │
│   └── tasktracker
│       ├── manage.py
│       │
│       ├── tasktracker
│       │   ├── settings.py
│       │   └── urls.py
│       │
│       └── tasks
│           ├── views.py
│           └── urls.py
│
├── frontend
│   │
│   └── dayy7
│       ├── package.json
│       └── src
│           ├── App.jsx
│           ├── App.css
│           └── main.jsx
│
└── notes.md
```

---

## 4. Django Backend API

The Django backend provides an API endpoint that returns task information in JSON format.

### API Endpoint

```text
http://127.0.0.1:8001/api/tasks/
```

### Example JSON Response

```json
{
  "status": "success",
  "tasks": [
    {
      "id": 1,
      "task_name": "Learn Django",
      "status": "Completed"
    },
    {
      "id": 2,
      "task_name": "Learn React",
      "status": "Pending"
    },
    {
      "id": 3,
      "task_name": "Connect React with Django",
      "status": "Pending"
    }
  ]
}
```

---

## 5. Django View

The Django view returns task data using `JsonResponse`.

```python
from django.http import JsonResponse

def task_list(request):
    data = {
        "status": "success",
        "tasks": [
            {
                "id": 1,
                "task_name": "Learn Django",
                "status": "Completed"
            },
            {
                "id": 2,
                "task_name": "Learn React",
                "status": "Pending"
            },
            {
                "id": 3,
                "task_name": "Connect React with Django",
                "status": "Pending"
            }
        ]
    }

    return JsonResponse(data)
```

---

## 6. Django URL Configuration

The API endpoint is connected to the Django view using URL routing.

### `tasks/urls.py`

```python
from django.urls import path
from .views import task_list

urlpatterns = [
    path("api/tasks/", task_list),
]
```

### `tasktracker/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
]
```

---

## 7. React Frontend

The React frontend uses `fetch()` to request task data from the Django backend.

### `App.jsx`

```jsx
import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8001/api/tasks/")
      .then((response) => response.json())
      .then((data) => {
        setTasks(data.tasks);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, []);

  return (
    <div className="app">
      <h1>Task Tracker</h1>
      <p>React + Django API Integration</p>

      {tasks.map((task) => (
        <div className="task-card" key={task.id}>
          <h3>{task.task_name}</h3>
          <p>Status: {task.status}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
```

---

## 8. How the Connection Works

The communication flow is:

```text
React Frontend
      |
      | fetch()
      ↓
Django API
      |
      | JSON Response
      ↓
React
      |
      ↓
Display Tasks
```

### Step-by-step flow

1. React application starts.
2. `useEffect()` runs when the component loads.
3. `fetch()` sends a GET request to the Django API.
4. Django receives the request.
5. Django view prepares task data.
6. Django returns JSON response.
7. React receives the JSON data.
8. `setTasks()` stores the task data in state.
9. `.map()` displays each task on the webpage.

---

## 9. useState()

`useState()` is used to store the tasks received from the Django API.

```jsx
const [tasks, setTasks] = useState([]);
```

Initially, the tasks array is empty.

After receiving the API response:

```jsx
setTasks(data.tasks);
```

the task data is stored in React state.

---

## 10. useEffect()

`useEffect()` is used to perform the API request when the React component loads.

```jsx
useEffect(() => {
  fetch("http://127.0.0.1:8001/api/tasks/")
    .then((response) => response.json())
    .then((data) => {
      setTasks(data.tasks);
    });
}, []);
```

The empty dependency array `[]` means the effect runs when the component is mounted.

---

## 11. Rendering API Data

The `.map()` method is used to display the tasks dynamically.

```jsx
{tasks.map((task) => (
  <div className="task-card" key={task.id}>
    <h3>{task.task_name}</h3>
    <p>Status: {task.status}</p>
  </div>
))}
```

The tasks are received from the Django API instead of being manually written in the JSX.

---

## 12. CORS

When React and Django run on different ports, the browser can block the request because they have different origins.

For example:

```text
React  → http://localhost:5173
Django → http://127.0.0.1:8001
```

CORS (Cross-Origin Resource Sharing) allows the frontend to communicate with the backend.

The `django-cors-headers` package can be used to configure CORS in Django.

---

## 13. Running the Backend

Open PowerShell and go to the Django project:

```powershell
cd "C:\Users\asus\Desktop\WEEK-4-PYTHON-DJANGO\DAY-6-REACT-DJANGO-API\backend\tasktracker"
```

Activate the virtual environment:

```powershell
..\venv\Scripts\Activate.ps1
```

Start Django:

```powershell
python manage.py runserver 8001
```

The backend runs at:

```text
http://127.0.0.1:8001/
```

---

## 14. Running the React Frontend

Open another terminal.

Go to the React project:

```powershell
cd "C:\Users\asus\Desktop\WEEK-4-PYTHON-DJANGO\DAY-6-REACT-DJANGO-API\frontend\dayy7"
```

Start the React development server:

```powershell
npm run dev
```

The React application normally runs at:

```text
http://localhost:5173/
```

---

## 15. Expected Output

After the React frontend successfully connects to the Django API, the browser should display:

```text
Task Tracker

React + Django API Integration

Learn Django
Status: Completed

Learn React
Status: Pending

Connect React with Django
Status: Pending
```

The task information should come from the Django API.

---

## 16. Testing the API

The Django API can be tested using a browser, curl, Postman, or another API testing tool.

API URL:

```text
http://127.0.0.1:8001/api/tasks/
```

Example command:

```powershell
curl.exe http://127.0.0.1:8001/api/tasks/
```

The API should return JSON data containing the tasks.

---

## 17. Day 6 Outcome

By completing Day 6, I learned how to:

* Connect a React frontend to a Django backend.
* Create and use a Django API endpoint.
* Send a GET request using `fetch()`.
* Receive JSON data from Django.
* Store API data using `useState()`.
* Fetch data using `useEffect()`.
* Display API data dynamically using `.map()`.
* Understand the purpose of CORS.
* Run React and Django applications separately.

---

## 18. Conclusion

Day 6 demonstrated how a frontend and backend communicate in a full-stack application.

React provides the user interface, while Django provides the API and backend logic. The `fetch()` function allows React to request data from Django, and JSON is used to transfer the data between the two applications.

This forms the basic foundation for building a full-stack Task Tracker application using React and Django.

---

**Intern:** Shahid Attar
**Intern ID:** C.ID: ZST/2026/DRM/KOP-0009
**Week:** 4
**Day:** 6
**Topic:** Connecting React with Django API
