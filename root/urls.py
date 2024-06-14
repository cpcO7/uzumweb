from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from root import settings

urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('', include('apps.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
