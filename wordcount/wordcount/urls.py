from django.contrib import admin
from django.urls import path
import wordcount_app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcount_app.views.home,name='home'),
    path('introduce/',wordcount_app.views.introduce, name = 'introduce'),
    path('profile/<int:designer_id>', wordcount_app.views.detail, name = 'detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
