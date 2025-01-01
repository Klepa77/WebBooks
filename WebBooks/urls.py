from django.contrib import admin
from django.urls import include,path
from catalog import views
# Добавлено для работы с медиа файлами
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include(('catalog.urls','catalog'),namespace='catalog')),
    path('admin/', admin.site.urls),
]
#Добавлено для работы с медиафайлами локально
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)