from django.db import models
from users.models import Executer, Customer
from django.db.models.signals import post_save
from django.dispatch import receiver


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    price = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='price')
    description = models.CharField(max_length=400, verbose_name='description')
    created_by = models.ForeignKey(Executer, verbose_name='executor')
    owner = models.ForeignKey(Customer, verbose_name='customer')

    def __str__(self):
        return self.title



@receiver(post_save, sender=Task)
def post_update(sender, instance, **kwargs):
    instance.owner.update_balance(instance.price, instance.owner.id)
    instance.created_by.update_balance(instance.price, instance.created_by.id)

