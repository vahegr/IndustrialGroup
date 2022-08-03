from django.urls import path, re_path
from . import views

app_name = 'article_app'

urlpatterns = [
    path('', views.all_articles, name='articles'),
    re_path(r'detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.article_detail, name='article_detail'),
    # re_path(r'^detail/(?P<id>[0-9]{4})/(?P<slug>[\w-]+)/$', views.article_detail),
]