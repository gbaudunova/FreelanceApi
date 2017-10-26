from django.db import models
from django.db.models import F




class Executer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='balance')

    def __str__(self):
        return self.first_name


    def update_balance(self, balance):
        Executer.objects.select_for_update(). \
            filter(pk=self.pk) \
            .update(balance=F('balance') + balance)


class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='balance')

    def __str__(self):
        return self.first_name


    def update_balance(self, balance):
        Customer.objects.select_for_update(). \
            filter(pk=self.pk) \
            .update(balance=F('balance') - balance)

