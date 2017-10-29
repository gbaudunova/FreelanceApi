from django.test import TestCase
from users.models import Executer, Customer
from task.models import Task
from django.test import Client
# import requests


class TestExecuterViewSet(TestCase):

    def test_for_queryset(self):
        a = Executer.objects.create(first_name='name', balance=300)
        self.assertEqual(a.first_name, 'name')
        self.assertEqual(a.balance, 300)


class TestCustomerViewSet(TestCase):
    def test_for_queryset(self):
        a = Customer.objects.create(first_name='name', balance=300)
        self.assertEqual(a.first_name, 'name')
        self.assertEqual(a.balance, 300)


class TestTaskViewSet(TestCase):
    def test_for_queryset(self):
        created_by = Executer.objects.create(
            first_name="First_name1", balance="1000")
        owner = Customer.objects.create(
            first_name="First_name2", balance="1000")
        a = Task.objects.create(title="Task_1", price=500, description="Description_1",
                                created_by=created_by, owner=owner)
        self.assertEqual(a.title, 'Task_1')
        self.assertEqual(a.price, 500)
        self.assertEqual(a.description, 'Description_1')
        self.assertEqual(a.created_by, created_by)
        self.assertEqual(a.owner, owner)


class ApiTest(TestCase):
    def test_of_whole_Api_endpoint(self):
        self.client = Client()
        response = self.client.get('http://127.0.0.1:8000/api/')
        # customer_responce = self.client.get('http://127.0.0.1:8000/api/customer/')
        # executer_responce = self.client.get('http://127.0.0.1:8000/api/executer/')
        # task_responce = self.client.get('http://127.0.0.1:8000/api/tasks/')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(customer_response.status_code, 200)
        # self.assertEqual(executer_response.status_code, 200)
        # self.assertEqual(task_response.status_code, 200)











