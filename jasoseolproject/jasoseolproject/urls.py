from django.contrib import admin
from django.urls import path,include
# include 함수를 통해서 url을 상속시켜준다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jsproject.urls')), 
    path('', include('accounts.urls')), 
]
