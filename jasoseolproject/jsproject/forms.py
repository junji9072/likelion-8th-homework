from django import forms # 모델폼을 쓰기 위해서 장고에서 불러온다.
from .models import Jasosel

class JssForm(forms.ModelForm):
    class Meta:
        model = Jasosel #어떤 모델과 대응될 지
        fields = ('title','content',) #모델 안에서 어떤 것만 사용하겠다. updated_at은 자동적으로 생성 되므로 사용자가 입력 할 필요없어서 사용 X
                                    # author 추가해주면 작성자를 추가해줄 수 있는데 그럼 큰일!
    def __init__(self,*args,**kwargs): #클래스에는 첫인자는 항상 self, *args,**kwargs는 여러 인자를 받을 수 있는 파라메터
        super().__init__(*args,**kwargs) #super는 부모클래스에서 가져와서 쓸 수 있음. 
        self.fields['title'].label = '제목'
        self.fields['content'].label = '자소서 내용'
        self.fields['title'].widget.attrs.update({
            'class' : 'jss_title',
            'placeholder' : '제목',
        })