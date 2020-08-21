from django import forms
from .models import SCH

class SchForm(forms.ModelForm):
    class Meta:
        model = SCH
        fields = ('image','name','major','year','studentid','grade','GPA')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].required = False
        self.fields['name'].label = '이름'
        self.fields['major'].label = '학과'
        self.fields['year'].label = '입학년도'
        self.fields['studentid'].label = '학번'
        self.fields['grade'].label = '학년'
        self.fields['GPA'].label = '평균학점'
        self.fields['name'].widget.attrs.update({
            'class' : 'sch_name',
            'placeholder' : '이름',
        })
        self.fields['major'].widget.attrs.update({
            'class' : 'sch_major',
            'placeholder' : '학과',
        })
        self.fields['year'].widget.attrs.update({
            'class' : 'sch_year',
            'placeholder' : '입학년도',
        })
        self.fields['studentid'].widget.attrs.update({
            'class' : 'sch_studentid',
            'placeholder' : '학번',
        })
        self.fields['grade'].widget.attrs.update({
            'class' : 'sch_grade',
            'placeholder' : '학년',
        })
        self.fields['GPA'].widget.attrs.update({
            'class' : 'GPA',
            'placeholder' : '평균학점',
        })