from __future__ import unicode_literals
from rest_framework import routers
from django.conf.urls import url, include
from api.views import ConverterViewSet, CustomerViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r'converter', ConverterViewSet, base_name='converter')
router.register(r'customer', CustomerViewSet, base_name='customer')
router.register(r'tasks', TaskViewSet, base_name='tasks')

urlpatterns = [
    # url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
    url(r'^', include(router.urls)),
]
urlpatterns = router.urls

