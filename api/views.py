from __future__ import unicode_literals
from rest_framework import viewsets
from .serializers import ExecuterSerializer, TaskSerializer, CustomerSerializer
from users.models import Customer, Executer
from task.models import Task


class ExecuterViewSet(viewsets.ModelViewSet):
    queryset = Executer.objects.all()
    serializer_class = ExecuterSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()

    serializer_class = CustomerSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    print(queryset)
    serializer_class = TaskSerializer

