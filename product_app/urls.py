from django.urls import path, re_path
from . import views

app_name = 'product_app'

urlpatterns = [
    path('', views.product_items, name='products'),
    re_path(r'detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
]