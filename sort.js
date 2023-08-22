
const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number).slice(1)

const solution = arr => {
  return arr.sort((a,b) => a-b).join("\n")
}

console.log(solution(input));
