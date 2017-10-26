from __future__ import unicode_literals
from rest_framework import routers
# from django.conf.urls import url, include
from api.views import ExecuterViewSet, CustomerViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r'executer', ExecuterViewSet, base_name='executer')
router.register(r'customer', CustomerViewSet, base_name='customer')
router.register(r'tasks', TaskViewSet, base_name='tasks')


urlpatterns = router.urls

