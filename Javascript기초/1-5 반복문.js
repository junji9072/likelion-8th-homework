for (const i = 0; i < 10; i++) { // const는 변하지 않는 값이므로 에러 발생
    console.log(i);
}

for (let i = 0; i < 10; i++) { // let으로 해야 실행된다.
    console.log(i);
}

const numInfo = {
    'one': 'first',
    'two': 'second',
    'three': 'third'
};

for (const i in numInfo) {
    // 왜 여기서는 const를 썼는데 적용이 되는건데? 위에서는 ++ 증감 연산자이고 여기서는 가져와서 읽을 뿐이므로 사용 가능하다.
    console.log(`기수: ${i}, 서수: ${numInfo[i]}`);
}

const oddNums = [1, 3, 5, 7, 9, 11];
for (const i of oddNums) {
    console.log(i);
}

//while 문
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}