#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

try {
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');
  const combinedContent = contentA + contentB;

  fs.writeFileSync(fileC, combinedContent);

  console.log(`Contents of ${fileA} and ${fileB} have been concatenated to ${fileC}`);
} catch (error) {
  console.error('An error occurred:', error.message);
  process.exit(1);
}
