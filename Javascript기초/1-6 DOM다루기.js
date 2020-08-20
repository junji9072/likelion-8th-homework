//ID로 DOM 객체 선택
let idObj = document.getElementById('name');

//class로 DOM 객체 선택
let classObj = document.getElementsByClassName('');

// css 선택자로 DOM 객체 선택
let selectorObj = document.querySelector('#main')

//사용할 수 있는 속성들
// style, innerText, innerHtml
selectorObj.style = 'color:yellow';
selectorObj.innerText = '헬로';
selectorObj.innerHTML = '<a href="https://www.naver.com">네이버로 가기</a>';

// a Tag의 href 속성 같은 각종 태그들의 속성들
aTag.href = 'http://www.naver.com';