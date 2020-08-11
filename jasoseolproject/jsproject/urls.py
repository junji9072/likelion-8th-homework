from django.contrib import admin
from django.urls import path
from .views import index, create, detail, delete, update, my_index
#동일 레벨에 존재하므로 .으로 써준다.
urlpatterns = [
    path('',index,name='index'),
    path('my_index', my_index, name='my_index'), #내 자기소개서만 볼 수 있도록 한다.
    path('create/',create,name = 'create'),
    path('detail/<int:jss_id>',detail,name = 'detail'), #<int:변수명> 변수명 쓰는 이유 함수 내에 어떤 변수명으로 받을지.
    path('delete/<int:jss_id>',delete,name = 'delete'), #url과 패스컨버터 변수를 넘겨주는 방법은 변수명 통일! 여기서 예를들어 int:hello 하면 views에서도 동일하게 변경
    path('update/<int:jss_id>',update,name = 'update'), 
]
