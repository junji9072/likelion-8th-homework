from django.shortcuts import render,redirect
from .forms import SchForm
from .models import SCH

# Create your views here.
def home(request):
    all_sch = SCH.objects.all()
    return render(request, 'home.html' ,{'all_sch':all_sch})

def create(request):
    if request.method == 'POST':
        filled_form = SchForm(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.image = request.FILES['image']
            filled_form.save()
            return redirect('home')
    sch_form = SchForm()
    return render(request, 'create.html',{'sch_form':sch_form})

def detail(request,sch_id):
    my_sch = SCH.objects.get(pk=sch_id)
    return render(request, 'detail.html',{'my_sch':my_sch})

def delete(request,sch_id):
    my_sch = SCH.objects.get(pk=sch_id) 
    my_sch.delete()
    return redirect('home') 

def update(request,sch_id):
    my_sch = SCH.objects.get(pk=sch_id) 
    sch_form = SchForm(instance=my_sch)
    if request.method == 'POST':
        updated_form = SchForm(request.POST, instance=my_sch) 
        if updated_form.is_valid():
            updated_form.save()
            return redirect('home')
    return render(request, 'update.html',{'sch_form':sch_form})