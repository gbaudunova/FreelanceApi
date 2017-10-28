from django.dispatch import Signal

task_completed = Signal(providing_args=['update_balance'])