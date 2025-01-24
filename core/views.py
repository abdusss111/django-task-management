from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, Task, User
from .permissions import IsAdmin, IsManager, IsEmployee
from .serializers import ProjectSerializer, TaskSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsManager]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsEmployee]


def task_management_view(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'projects': projects,
        'tasks': tasks,
    }
    return render(request, 'core/index.html', context)


def auth_view(request):
    return render(request, 'core/auth.html')
