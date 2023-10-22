// const fs = require('fs');
// const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("").map(Number);
const input = fs.readFileSync('./input.txt').toString().trim().split('\r\n').map(Number).slice(1);
// const input = fs.readFileSync('./input.txt').toString().trim().split('').map(Number)

const solution = arr => {
    return arr.sort((a,b) => b-a).join("")    
}
  


console.log(solution(input));