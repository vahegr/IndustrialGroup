from django.urls import path, re_path
from . import views

app_name = 'contact_app'

urlpatterns = [
    path('', views.contact_us, name='contactus')
]