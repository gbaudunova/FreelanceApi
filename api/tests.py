from django.test import TestCase
from .views import ExecuterViewSet, CustomerViewSet, TaskViewSet
from users.models import Executer, Customer
from task.models import Task


# class ExecuterViewSet(viewsets.ModelViewSet):
#     queryset = Executer.objects.all()
#     serializer_class = ExecuterSerializer

class TestExecuterViewSet(TestCase):

    def test_should_send_executer_data(self):
        a = Executer.objects.create(first_name='name', balance=300)
        self.assertEqual(a.get('name').status_code, 200)

        # def test_get_results(self):
        #     c = User.objects.all()
        #     for u in c:
        #         self.assertEqual(u.get('username').status_code, 200)
        #     t = Task.objects.all()
        #     for j in t:
        #
        #     self.assertEqual(j.get('title').status_code, 200)



