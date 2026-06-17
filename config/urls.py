from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls', namespace='portal')),
    path('directories/', include('directories.urls', namespace='directories')),
    path('repositories/', include('repositories.urls', namespace='repositories')),
]

# Serve media files during development stage
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)