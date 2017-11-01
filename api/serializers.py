from users.models import Customer, Executer
from task.models import Task
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'balance')


class ExecuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executer
        fields = ('id', 'first_name', 'balance')


class TaskSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(read_only=True)
    # executer = ExecuterSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'price', 'owner', 'created_by')


