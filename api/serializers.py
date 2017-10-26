from users.models import Customer, Executer
from task.models import Task
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'




class ExecuterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executer
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(read_only=True)

    # executer = ExecuterSerializer(read_only=True)



    class Meta:
        model = Task
        fields = '__all__'

