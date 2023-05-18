from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

app_name= 'vimad_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vimad_app.urls', namespace='vimad_app')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)