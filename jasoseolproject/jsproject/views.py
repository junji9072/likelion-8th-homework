from django.shortcuts import render,redirect, get_object_or_404
from .forms import JssForm, CommentForm
from .models import Jasosel, Comment
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
    # try: 
    #     my_jss = Jasosel.objects.get(pk=jss_id) # 하나의 오브젝트/데이터만 전송 pk를 동적으로 변경
    #     return render(request,'detail.html',{'my_jss':my_jss}) #각 데이터마다 만드는게 아닌 공통으로 1개만 만들어서 활용
    # except:
    #     raise Http404 # 없는 오브젝트/데이터면 404에러 나오도록 한다.
    # my_jss = get_object_or_404(Jasosel, pk=jss_id)
    my_jss = get_object_or_404(Jasosel, pk=jss_id)
    comment_form = CommentForm()

    return render(request, 'detail.html', {'my_jss':my_jss, 'commet_form':comment_form})#comment_form 이라는 키 값으로 템플릿에 보내줌

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

#POST로 했으니 detail 재사용 가능하지만 분리해서 써보자.
def create_comment(request, jss_id):
    # if request.method == 'POST': 안써도 OK
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid(): # 유효성 검증을 하면 save를 쓸 수 있다.
        temp_form = comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.jasoseol = Jasosel.objects.get(pk=jss_id) # detail.html 에서 뿌려진 자소설 객체를 넣어줘야한다.
        temp_form.save()
        return redirect('detail', jss_id) #특정 오브젝트를 가진 곳으로 건네준다.

def delete_comment(request, jss_id, comment_id):# 리다이렉션을 위한 자소설 id도 가져오고 댓글을 삭제할 것이므로 어떤 오브젝트 인지 알기 위해 id가 필요
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.author:
        my_comment.delete()
        return redirect('detail', jss_id)

    else:
        raise PermissionDenied
        