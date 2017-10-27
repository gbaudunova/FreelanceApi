from django.test import TestCase
from .models import Executer, Customer
# from django.db import models
# from . import models
# from django.dispatch import receiver
# from django.db.models.signals import post_save

class ExecuterTest(TestCase):

    def test_executer_creation(self):
        a = Executer.objects.create(first_name="Igor", balance=1000)
        self.assertEqual(a.first_name, 'Igor')
        self.assertEqual(a.balance, 1000)





class CustomerTest(TestCase):

    def test_customer_creation(self):
        b = Customer.objects.create(first_name="Anna", balance=1000)
        self.assertEqual(b.first_name, 'Anna')
        self.assertEqual(b.balance, 1000)


