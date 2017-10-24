from users.models import Customer, Executer
from task.models import Task
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'balance')


class ExecuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executer
        fields = ('first_name', 'balance')


class TaskSerializer(serializers.ModelSerializer):
    owner = ExecuterSerializer(read_only=True)
    owner = CustomerSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('title', 'price', 'description', 'owner', 'created_by')


