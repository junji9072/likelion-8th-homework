# 멋쟁이 사자처럼 CRUD #2
## -Django를 활용해 Create, Read, Update, Delete를 구현해 봅시다.-

🙋‍♀️지난 시간 리뷰🙋‍♂️

CRUD

Create / Read / Update / Delete

GET / POST

클라이언트에서 서버로 요청을 보내는 방법

📚오늘의 강의

CRUD 구현

패키지 종속성 관리

✍ UPDATE

정보 수정이 필요한 객체를 찾아 Data를 새롭게 저장

1. 객체 탐색 : post = get_object_or_404(Designer, pk = designer_id)

                        if request.methoe == 'POST':

2. 입력 Data 저장 : [post.name](http://post.name) = request.POST['name']

                         post.address = request.POST['address'] ....

3. 입력 Data 저장 : post.save()

✍ 패키지 종속성 관리

내 환경에서 어떤 패키지를 어떤 버전으로 사용하고 있는지 알려주는 것

패키지 설치 : pip install -r requirements.txt

패키지 정의 : pip freeze > requirements.txt