# эти 2 для загрузки медиа
from django.conf.urls.static import static
from dj_women import settings

from django.contrib import admin
from django.urls import path, include

from women.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls'))
]

# ДЛЯ добавки МЕДИА файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
