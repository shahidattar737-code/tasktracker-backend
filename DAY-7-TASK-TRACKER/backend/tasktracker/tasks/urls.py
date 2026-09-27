from django.urls import path
from .views import task_list, task_detail

urlpatterns = [
    path("api/tasks/", task_list),
    path("api/tasks/<int:task_id>/", task_detail),
]