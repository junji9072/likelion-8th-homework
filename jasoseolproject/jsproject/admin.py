from django.contrib import admin
from .models import Jasosel #다른 파일에서 만든거니 불러오자. 동일한 레벨에 존재하므로 .을 사용
# Register your models here.

admin.site.register(Jasosel) #admin페이지에 모델을 등록