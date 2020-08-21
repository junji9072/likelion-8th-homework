from django.urls import path
from .views import home, create, detail, delete, update

urlpatterns = [
    path('',home,name='home'),
    path('create/',create,name='create'),
    path('detail/<int:sch_id>',detail,name = 'detail'),
    path('delete/<int:sch_id>',delete,name = 'delete'), 
    path('update/<int:sch_id>',update,name = 'update'),
]