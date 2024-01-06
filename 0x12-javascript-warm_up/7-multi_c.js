#!/usr/bin/node

const args = process.argv.slice(2);
const numberOfTimes = parseInt(args[0]);

if (isNaN(numberOfTimes)) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < numberOfTimes; i++) {
        console.log("C is fun");
    }
}
