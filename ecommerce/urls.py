from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_prometheus import exports

urlpatterns = [
    path('metrics/', exports.ExportToDjangoView, name='prometheus-metrics'),
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
