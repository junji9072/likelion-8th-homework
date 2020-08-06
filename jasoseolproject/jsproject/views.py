from django.shortcuts import render,redirect
from .forms import JssForm
from .models import Jasosel
from django.http import Http404

# Create your views here.
def index(request):
    all_jss = Jasosel.objects.all()
    return render(request,'index.html',{'all_jss':all_jss})
def create(request):
    if request.method == 'POST':
        filled_form = JssForm(request.POST)
        if filled_form.is_valid(): # is_valid함수를 통해 유효성 검사
            filled_form.save()
            return redirect('index') # index로 단순히 보내주기 때문에 redirect

    jss_form = JssForm()
    return render(request,'create.html',{'jss_form':jss_form})
def detail(request,jss_id):
    try:
        my_jss = Jasosel.objects.get(pk=jss_id)
        return render(request,'detail.html',{'my_jss':my_jss}) #각 데이터마다 만드는게 아닌 공통으로 1개만 만들어서 활용
    except:
        raise Http404
def delete(request,jss_id):
    my_jss = Jasosel.objects.get(pk=jss_id)
    my_jss.delete()
    return redirect('index')

def update(request,jss_id):
    my_jss = Jasosel.objects.get(pk=jss_id)
    jss_form = JssForm(instance=my_jss)
    if request.method == 'POST':
        updated_form = JssForm(request.POST, instance=my_jss)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request, 'create.html',{'jss_form':jss_form})