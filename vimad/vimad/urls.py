from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('vimad_app/', include('vimad_app.urls')),
    path('admin/', admin.site.urls),
]
