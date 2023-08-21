const fs = require('fs');
// const input = require("fs").readFileSync("/dev/stdin", "utf-8").trim().split("\n");
const input = fs.readFileSync('./input.txt').toString().trim().split('\r\n');
let  array1 = input[1].split(' ');
let count = input[0].split(' ')[0];
let cutline = input[0].split(' ')[1];


array1.sort((a,b)=>b-a);
console.log(array1[cutline-1]);