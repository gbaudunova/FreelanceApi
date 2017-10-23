from django.db import models



class Executer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='balance')

    def __str__(self):
        return self.first_name


class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='name')
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='balance')

    def __str__(self):
        return self.first_name