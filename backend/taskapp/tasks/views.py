from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Task

# Get all tasks
def get_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)

# Create a new task
@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task = Task.objects.create(title=data['title'], completed=data.get('completed', False))
        return JsonResponse({"id": task.id, "title": task.title, "completed": task.completed})

# Update a task
@csrf_exempt
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        task.completed = data.get('completed', task.completed)
        task.save()
        return JsonResponse({"id": task.id, "title": task.title, "completed": task.completed})

# Delete a task
@csrf_exempt
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "DELETE":
        task.delete()
        return JsonResponse({"message": "Task deleted"})

