#!/usr/bin/node

function findSecondLargest(args)
{
    if (args.length <= 1)
    {
        return 0;
    }

    let uniqueArgs = [...new Set(args)];
    uniqueArgs.sort((a, b) => b - a);
    return uniqueArgs[1];
}

const args = process.argv.slice(2).map(Number);
console.log(findSecondLargest(args));
