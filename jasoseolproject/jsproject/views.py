from django.shortcuts import render,redirect
from .forms import JssForm
from .models import Jasosel
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required 

# Create your views here.
def index(request):
    all_jss = Jasosel.objects.all()
    return render(request,'index.html',{'all_jss':all_jss})

def my_index(request):
    my_jss = Jasosel.objects.filter(author=request.user) # 특정 조건을 만족시키는 필터로 가져온다. 자소설 오브젝트 안에서 auhtor라는 필드에 현재로그인된 유저만 가져오겠다. 
    return render(request, 'index.html', {'all_jss':my_jss})# 인덱스 페이지에서 all_jss라는 for문을 돌렸기 때문에 all_jss로 가져와야한다.

@login_required(login_url='/login/')#(url 경로 지정안해주면 오류가 뜬다)
def create(request):
    # if not request.user.is_authenticated: 인증이 안되있으면
    #       return redirect('login') 로그인페이지로 넘겨줌
    if request.method == 'POST':
        filled_form = JssForm(request.POST)
        if filled_form.is_valid(): # is_valid함수를 통해 유효성 검사
            temp_form = filled_form.save(commit=False) #commit=False를 넣어주면 저장전 생성 업뎃 전 사이 뭔가를 해줄 수 있다.
            temp_form.author = request.user
            temp_form.save()
            return redirect('index') # index로 단순히 보내주기 때문에 redirect

    jss_form = JssForm()
    return render(request,'create.html',{'jss_form':jss_form})

@login_required(login_url='/login/')
def detail(request,jss_id):
    try: 
        my_jss = Jasosel.objects.get(pk=jss_id) # 하나의 오브젝트/데이터만 전송 pk를 동적으로 변경
        return render(request,'detail.html',{'my_jss':my_jss}) #각 데이터마다 만드는게 아닌 공통으로 1개만 만들어서 활용
    except:
        raise Http404 # 없는 오브젝트/데이터면 404에러 나오도록 한다.
    # my_jss = get_object_or_404(Jasosel, pk=jss_id)
def delete(request,jss_id):
    my_jss = Jasosel.objects.get(pk=jss_id) #my_jss를 pk를 통해 잘 가져왔고, 
    if request.user == my_jss.author: #만약 my_jss 가져온 객체와 author 같다면 지워줌
        my_jss.delete() #이 함수를 통해 삭제
        return redirect('index') #url 을 통해서도 삭제 가능!
    raise PermissionDenied # 아니라면 권한을 위반했다는걸 일으킨다.
def update(request,jss_id):
    my_jss = Jasosel.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss) #인스턴스를 이용해서 수정시에 이전 글이 남아있도록 함.
    if request.method == 'POST': #수정하고 난 뒤 확인 버튼을 누르면 post방식으로 요청
        updated_form = JssForm(request.POST, instance=my_jss) # 인스턴스를 인자로 넘겨주지 않으면, 새로운 것으로 인식
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request, 'create.html',{'jss_form':jss_form}) #create페이지를 모델 폼을 이용해서 재활용