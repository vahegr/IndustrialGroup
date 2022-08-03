from django.urls import path
from . import views

app_name = 'services_app'

urlpatterns = [
    path('', views.services, name='services'),
]