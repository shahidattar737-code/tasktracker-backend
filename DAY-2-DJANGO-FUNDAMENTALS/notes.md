# Day 2 — Django Fundamentals

## Topic

Django Project, Apps, URLs, and Views

---

## 1. Django Project

A Django project contains the configuration and settings required for a Django backend application.

For this task, a Django project named `tasktracker` was created.

### Command Used

```bash
django-admin startproject tasktracker
```

---

## 2. Django Application

A Django application is a component inside a Django project that handles a specific functionality.

For the Task Tracker backend, an application named `tasks` was created.

### Command Used

```bash
python manage.py startapp tasks
```

The `tasks` application was added to `INSTALLED_APPS` in `settings.py`.

---

## 3. URLs

Django URL routing connects incoming requests to the appropriate view.

The root URL `/` was connected to the `home` view.

### URL Configuration

```python
from django.contrib import admin
from django.urls import path
from tasks.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```

---

## 4. Views

A Django view receives a request and returns a response.

A `home` view was created in `tasks/views.py`.

### View Code

```python
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Task Tracker Backend is running"
    })
```

---

## 5. Request-Response Flow

The basic flow learned today was:

```text
Client / Browser
       ↓
     URL
       ↓
   Django urls.py
       ↓
      View
       ↓
   JSON Response
```

---

## 6. Running the Django Server

The development server was started using:

```bash
python manage.py runserver
```

The application was tested in the browser at:

```text
http://127.0.0.1:8000/
```

The following JSON response was received:

```json
{
    "message": "Task Tracker Backend is running"
}
```

---

## Day 2 Outcome

* Django project created.
* `tasks` application created.
* `tasks` app added to `INSTALLED_APPS`.
* URL routing configured.
* `home` view created.
* JSON response returned from the view.
* Django development server tested successfully.
