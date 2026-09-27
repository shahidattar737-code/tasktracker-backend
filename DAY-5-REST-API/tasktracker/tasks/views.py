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