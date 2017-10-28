from django.db import models
from django.db.models import F
from myblog.signals import task_completed
from django.contrib.messages import success


class Executer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='balance')

    def __str__(self):
        return self.first_name

    def update_balance(self, balance, id):
        Executer.objects.select_for_update(). \
            filter(pk=id)\
            .update(balance=F('balance') + balance)

        if success:
            task_completed.send_robust(
                sender=id,
                balance=balance,
            )


class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='balance')

    def __str__(self):
        return self.first_name

    def update_balance(self, balance, id):
        Customer.objects.select_for_update(). \
            filter(pk=id) \
            .update(balance=F('balance') - balance)

        if success:
            task_completed.send_robust(
                sender=id,
                balance=balance,
            )

