from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    return Response(TaskSerializer(tasks, many=True).data)

@api_view(['POST'])
def add_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# Create your views here.
