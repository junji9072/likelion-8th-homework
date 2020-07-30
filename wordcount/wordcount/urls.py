from django.contrib import admin
from django.urls import path,include
import wordcount_app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('wordcount_app.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
