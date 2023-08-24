const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim()
				.split('\n').slice(1).map(el => el.split(' ').map(Number))

const solution = input => {  
  return input.sort((a, b) => {
    if (a[0] === b[0]) {
      if(a[1] < b[1]) return -1;
    }
    return a[0] - b[0]
  }).map(el => el.join(' ')).join('\n')                              
}

console.log(solution(input))


