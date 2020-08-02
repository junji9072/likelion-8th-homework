from django.db import models

# Create your models here.
class Jasosel(models.Model): #modesl의 Model을 상속 받아 사용
    title = models.CharField(max_length = 50) #단순한 문자열이고 항상 max_Length로 제한을 줘야한다. 제목이니 길지 않게 50자로 제한
    content = models.TextField() #글자수 제한 없도록 만들테니 textfield
    updated_at = models.DateTimeField(auto_now= True) #날짜와 시간을 받을 수 있는 필드 생성 auto_now라는 옵션은 생성 수정시 날짜와 시간 자동 업뎃
