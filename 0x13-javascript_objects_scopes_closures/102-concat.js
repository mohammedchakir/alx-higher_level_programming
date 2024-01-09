#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, fileA) => {
  if (err) throw err;
  fs.readFile(fileB, 'utf8', (err, fileB) => {
    if (err) throw err;
    const content = fileA + fileB;
    fs.writeFile(fileC, content, (err) => {
      if (err) throw err;
    });
  });
});
