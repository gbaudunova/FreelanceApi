from users.models import Customer, Executer
from task.models import Task
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'balance', 'id')



class ExecuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executer
        fields = ('first_name', 'balance', 'id')


class TaskSerializer(serializers.ModelSerializer):
    created_by = ExecuterSerializer()
    owner = CustomerSerializer()

    class Meta:
        model = Task
        fields = ('title', 'price', 'description', 'created_by' 'owner')


