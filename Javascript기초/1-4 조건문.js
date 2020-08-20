//prompt 를 사용하는데 파이썬 Input과 비슷
let score = prompt('점수를 입렿가세요. 1', 0);
if (score >= 90) {
    console.log('A+');
} else if (score >= 80) {
    console.log('B+');
} else {
    console.log('C+');
}

//중첩된 if문으로 해석
score = promt('점수를 입렿가세요. 2', 0);
if (score >= 90) {
    console.log('A+');
} else {
    // 아래와 같이 실행할 문장이 한 문장이라면
    // 중괄호를 생략해도 된다.
    if (score >= 80)
        console.log('B+');
    else
        console.log('C+');
}