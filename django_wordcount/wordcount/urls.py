from django.contrib import admin
from django.urls import path
import wordcountprac.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcountprac.views.home, name="home"),
    path('about/',wordcountprac.views.about, name="about"),
    path('result/',wordcountprac.views.result, name="result")
]
