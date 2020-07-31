# 멋쟁이 사자처럼 CRUD #1
## -Django를 활용해 Create, Read, Update, Delete를 구현해 봅시다.-

🙋‍♀️지난 시간 리뷰🙋‍♂️

URL Include

App 별로 URL을 관리할 수 있도록 구조화

Template 상속

뼈대가 되는 Base.html을 생성해 다른 페이지에서 Extends로 불러오기

📚오늘의 강의

CRUD 개념 이해

GET / POST 이해

✍ CRUD란?

Create

Read

Update

Delete

✍ GET / POST

클라이언트에서 서버로 요청을 보내는 방법

📌 GET

Data를 'URL'에 포함시켜 전송

전송하는 길이에 제약 존재

Caching 가능(REST에서 데이터 조회에 활용) -값을 저장하는 기능-

→ READ에서 활용

📌 POST

Data를 'Body'에 넣어 전송 (URL에서 노출 X)

전송하는 길이에 제약 없음

Caching 불가능(REST에서 데이터 생성에 활용)

→ CREATE / UPDATE에서 활용

✍ CREATE

새로운 객체를 생성해 Data를 저장

1. 객체 생성 : if request.method == 'POST' :

                          post = Designer()

2. 입력 Data 저장 : [post.name](http://post.name) = request.POST['name']

                               post.address = request.POST['address'] ...

3. 입력 Data 저장 : post.save()

✍ UPDATE

정보 수정이 필요한 객체를 찾아 Data를 새롭게 저장

1. 객체 탐색 : post = get_object_or_404(Designer, pk = designer_id)

                       if request.methoe == 'POST':

2. 입력 Data 저장 : [post.name](http://post.name) = request.POST['name']

                               post.address = request.POST['address'] ....

3. 입력 Data 저장 : post.save()

✍ DELETE

제거가 필요한 객체를 찾아 삭제

1. 객체 탐색 : post = get_object_or_404(Designer, pk = designer_id)
2. 객체 삭제 : post.delete()
3. Home 으로 이동 : return redirect('home')