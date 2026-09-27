# Day 1 — Python Backend Setup

## Topic

Python Backend Setup — Virtual Environment, pip, and Django Installation

---

## 1. Python Backend

Python can be used to build web backends and APIs.

In this day, I prepared the Python environment required for backend development using Django.

---

## 2. Virtual Environment

### What is it?

A virtual environment is an isolated Python environment created for a project.

### Why do we use it?

It helps keep project dependencies separate from other Python projects.

### When do we use it?

We use a virtual environment when starting a Python project so that its packages can be managed separately.

### Command Used


python -m venv venv


To activate the virtual environment on Windows:


venv\Scripts\activate


After activation, `(venv)` appears in the terminal.

---

## 3. pip

### What is pip?

pip is Python's package installer. It is used to install and manage Python packages.

### Command Used


python -m pip --version


The pip version was checked inside the virtual environment.

### Update pip


python -m pip install --upgrade pip


In this setup, pip was already up to date.

---

## 4. Django

### What is Django?

Django is a Python web framework used to build web applications and backend APIs.

### Why do we use Django?

Django provides a structured framework for developing Python web applications and backend systems.

### When do we use Django?

Django can be used when building a Python-based web backend or API.

### Django Installation

python -m pip install django


### Django Version Check

django-admin --version


python -m django --version


Installed Django version:

**6.1.1**

---

## 5. requirements.txt

The installed Python packages were saved in `requirements.txt`.

### Command Used


python -m pip freeze > requirements.txt
