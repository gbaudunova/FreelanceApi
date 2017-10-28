from django.test import TestCase
from .models import Task
from users.models import *
from myblog.signals import task_completed


class TaskTest(TestCase):

    def test_task_creation(self):
        created_by = Executer.objects.create(
            first_name="First_name1", balance="1000")
        owner = Customer.objects.create(
            first_name="First_name2", balance="1000")
        Task.objects.create(title="Task_1", price="500", description="Description_1",
                            created_by=created_by, owner=owner)


class SignalTest(TestCase):

    def test_should_send_signal_when_balance_updated(self):
        self.signal_was_called = False
        self.balance = None

        def handler(sender, balance, **kwargs):
            self.signal_was_called = True
            self.balance = balance

        task_completed.connect(handler)

        c = Customer.objects.create(balance='1000', id=1)

        c.update_balance(1000, 1)

        self.assertTrue(self.signal_was_called)
        self.assertEqual(self.balance, 1000)

        task_completed.disconnect(handler)


class SignalTests(TestCase):
    def test_should_send_signal_when_balance_updated(self):
        self.signal_was_called = False
        self.balance = None

        def handler(sender, balance, **kwargs):
            self.signal_was_called = True
            self.balance = balance

        task_completed.connect(handler)

        a = Executer.objects.create(balance="2000", id=1)

        a.update_balance(2000, 1)

        self.assertTrue(self.signal_was_called)
        self.assertEqual(self.balance, 2000)

        task_completed.disconnect(handler)



