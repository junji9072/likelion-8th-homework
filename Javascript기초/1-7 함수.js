// 새로운 노드를 추가해주는 함수
function ver1_appendNewNdoe(target, tag = 'p', text = '기본값') {
    let newTag = document.createElement(tag);
    newTag.innerText = text;

    target.appendChild(newTag);
}

appendNewNode(target);
appendNewNode(target, 'a');
appendNewNode(target, 'a', 'A태그!');

// 익명함수의 형태
let var2_appendNewNdoe = function (target, tag = 'p', text = '기본값') {
    let newTag = document.createElement(tag);
    newTag.innerText = text;
    target.appendChild(newTag);
}
// 익명함수 2 : 화살표 함수 형태
let var3_appedNewNode = (target, tag = 'p', text = '기본값') => {
    let newTag = document.createElement(tag);
    newTag.innerText = text;
    target.appendChild(newTag);
}