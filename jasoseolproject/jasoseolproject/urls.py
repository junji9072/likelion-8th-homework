from django.contrib import admin
from django.urls import path
from jsproject.views import index, create, detail, delete, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('create/',create,name = 'create'),
    path('detail/<int:jss_id>',detail,name = 'detail'), #<int:변수명> 변수명 쓰는 이유 함수 내에 어떤 변수명으로 받을지.
    path('delete/<int:jss_id>',delete,name = 'delete'), #url과 패스컨버터 변수를 넘겨주는 방법은 변수명 통일! 여기서 예를들어 int:hello 하면 views에서도 동일하게 변경
    path('update/<int:jss_id>',update,name = 'update'), 
]
