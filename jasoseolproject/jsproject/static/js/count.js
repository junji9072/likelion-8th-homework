//alert("hello world") // hello world라는 경고창을 띄워준다.

const targetForm = document.querySelector('.jss_content_form') 
/* . 클래스로 지정해준다. 아이디로 하고 싶으면 #
 변수 지정시 JS는 const와 let 두가지 방식으로 지정해준다. 
 const는 변하지 않는 값 let 값이 변하는 값
 만약 잘 들어갔는지 확인해보고 싶다! console.log(targetForm) 통해 확인 가능
 */
const counted_text = document.querySelector('.counted_text')

targetForm.addEventListener("keyup", function() { // 요소.addEventListener('이벤트',이벤트를 감지했을 때 실행되는 함수)
                        //keyup 키보드를 눌렀다 떼었을 때
    counted_text.innerHTML = targetForm.value.length //안에 존재하는 html을 글자수를 세어준다.
})