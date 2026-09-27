from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def request_handler(request):

    if request.method == "GET":
        return JsonResponse({
            "method": "GET",
            "message": "GET request received"
        })

    elif request.method == "POST":
        return JsonResponse({
            "method": "POST",
            "message": "POST request received"
        })

    elif request.method == "PUT":
        return JsonResponse({
            "method": "PUT",
            "message": "PUT request received"
        })

    elif request.method == "DELETE":
        return JsonResponse({
            "method": "DELETE",
            "message": "DELETE request received"
        })

    return JsonResponse({
        "message": "Method not allowed"
    }, status=405)