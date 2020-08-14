from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jasosel(models.Model): #modesl의 Model을 상속 받아 사용
    title = models.CharField(max_length = 50) #단순한 문자열이고 항상 max_Length로 제한을 줘야한다. 제목이니 길지 않게 50자로 제한
    content = models.TextField() #글자수 제한 없도록 만들테니 textfield
    updated_at = models.DateTimeField(auto_now= True) #날짜와 시간을 받을 수 있는 필드 생성 auto_now라는 옵션은 생성 수정시 날짜와 시간 자동 업뎃
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 자소설 모델과 장고 유저모델과 FK로 연결시켜 주고 싶음 첫 인자로 연결 해주고 싶은 모델
    # on_delete 혹시 연결된 모델이 지워지면 그 오브젝트는 어쩔꺼냐. 작성자가 탈퇴하면 작성글은 작성자가 탈퇴시 삭제해주겠다.
    # null =True 옵션을 주면 작성자가 없어도 글 작성 가능.

class Comment(models.Model):
    content = models.CharField(max_length=100) #하나의 댓글 창
    author = models.ForeignKey(User, on_delete=models.CASCADE) #댓글은 작성자가 1명이 아님 1명의 작성자가 여러 댓글 쓸 수 있으므로 FK
    jasoseol = models.ForeignKey(Jasosel, on_delete=models.CASCADE) # 자소설 객체 1개 있으면, 하나의 자소서 글에 연결된 댓글들이 존재할텐데 그런 관계를 생각해서 FK

#파이썬 파일이므로 comment 모델이 Jasosel모델 보다 상위에 있으면 실행이 되지 않는다! 파이썬은 차례로 실행되기 때문.