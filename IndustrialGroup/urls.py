from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('about/', include('about_app.urls')),
    path('services/', include('services_app.urls')),
    path('products/', include('product_app.urls')),
    path('articles/', include('article_app.urls')),
    path('contactus/', include('contact_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
