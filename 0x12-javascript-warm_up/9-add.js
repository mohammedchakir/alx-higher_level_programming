#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const args = process.argv.slice(2);
const firstInteger = parseInt(args[0]);
const secondInteger = parseInt(args[1]);

console.log(add(firstInteger, secondInteger));
