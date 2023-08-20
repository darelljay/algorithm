//  내 코드 뭐가 틀린건지 정말 진지하게 하나도 모르겠으나 결과는 똑같이 나온다
// const fs = require('fs');
// const input = fs.readFileSync('./input.txt').toString().trim().split('\r\n')

// let sum = Number(0);
// for(let i=0; i<input.length; i++){
//     sum+=Number(input[i]);
// }
// input.sort();
// console.log(parseInt(sum/input.length)+'\n'+input[parseInt(input.length/2)]);


const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");

let mode = 0, total = 0;

for(let i = 0; i < input.length; i++){
	total += Number(input[i]);
}

const forSort = input.sort((a, b) => a - b);
mode = Math.floor(input.length / 2);
console.log(total / input.length);
console.log(forSort[mode]);