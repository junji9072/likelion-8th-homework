from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView #login.html 경로 이동을 위해 불러온다.
# 항상 contrib.auth 유저 관련된 것들이 들어가 있다고 생각
# # Create your views here.
def signup(request):
    regi_form = UserCreationForm() #유저 모델이 만들어져 있고 여러 기능이 장고에서 제공해준다.
    if request.method == "POST": #POST방식으로 넘어오면
        filled_form = UserCreationForm(request.POST)  
        if filled_form.is_valid(): #필드폼의 유효성 검증
            filled_form.save()
            return redirect('index')
    # 굳이 else 쓰지 않아도 실행 가능하다.
    return render(request, 'signup.html', {'regi_form':regi_form})

class MyLoginView(LoginView): #상속 로그인 뷰의 특성을 가지고 있다.
    template_name = 'login.html'