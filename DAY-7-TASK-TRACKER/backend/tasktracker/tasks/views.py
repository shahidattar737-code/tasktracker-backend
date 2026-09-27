import json
from django.http import JsonResponse
from .models import Task


def task_list(request):
    # GET - View all tasks
    if request.method == "GET":
        tasks = Task.objects.all()

        data = []

        for task in tasks:
            data.append({
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date,
            })

        return JsonResponse({
            "status": "success",
            "tasks": data
        })


    # POST - Create new task
    elif request.method == "POST":
        body = json.loads(request.body)

        task = Task.objects.create(
            task_name=body["task_name"],
            description=body["description"],
            status=body["status"]
        )

        return JsonResponse({
            "status": "success",
            "message": "Task created successfully",
            "task": {
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date,
            }
        }, status=201)


def task_detail(request, task_id):

    try:
        task = Task.objects.get(id=task_id)

    except Task.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Task not found"
        }, status=404)


    # PUT - Update task
    if request.method == "PUT":
        body = json.loads(request.body)

        task.task_name = body.get("task_name", task.task_name)
        task.description = body.get("description", task.description)
        task.status = body.get("status", task.status)

        task.save()

        return JsonResponse({
            "status": "success",
            "message": "Task updated successfully",
            "task": {
                "id": task.id,
                "task_name": task.task_name,
                "description": task.description,
                "status": task.status,
                "created_date": task.created_date,
            }
        })


    # DELETE - Delete task
    elif request.method == "DELETE":
        task.delete()

        return JsonResponse({
            "status": "success",
            "message": "Task deleted successfully"
        })


    return JsonResponse({
        "status": "error",
        "message": "Method not allowed"
    }, status=405)