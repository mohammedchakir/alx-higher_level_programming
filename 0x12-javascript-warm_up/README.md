## *0x12. JavaScript - Warm up*

By Guillaume


## *Background Context:*

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

-   Scripting (same as we did with Python)
-   Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg)

## *Resources:*
Read or watch:

-   [Writing JavaScript Code]()
-   [Variables]()
-   [Data Types]()
-   [Operators]()
-   [Operator Precedence]()
-   [Controlling Program Flow]()
-   [Functions]()
-   [Objects and Arrays]()
-   [Intrinsic Objects]()
-   [Module patterns]()
-   [var, let and const]()
-   [JavaScript Tutorial]()
-   [Modern JS]()


## *General:*

-   Why JavaScript programming is amazing
-   How to run a JavaScript script
-   How to create variables and constants
-   What are differences between `var`, `const` and `let`
-   What are all the data types available in JavaScript
-   How to use the `if`, `if ... else` statements
-   How to use comments
-   How to affect values to variables
-   How to use `while` and `for` loops
-   How to use `break` and `continue` statements
-   What is a function and how do you use functions
-   What does a function that does not use any `return` statement return
-   Scope of variables
-   What are the arithmetic operators and how to use them
-   How to manipulate dictionary
-   How to import a file


## *More Info:*

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### Install semi-standard

[Documentation]()

```
$ sudo npm install semistandard --global

```

## *Tasks:*


#### [0. First constant, first print](0-javascript_is_amazing.js)

Write a script that prints "JavaScript is amazing":

-   You must create a constant variable called `myVar` with the value "JavaScript is amazing"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
JavaScript is amazing
@ubuntu:~/0x12$
@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
@ubuntu:~/0x12$

```


#### [1. 3 languages](1-multi_languages.js)

Write a script that prints 3 lines:

-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
@ubuntu:~/0x12$

```

#### [2. Arguments](2-arguments.js)

Write a script that prints a message depending of the number of arguments passed:

-   If no arguments are passed to the script, print "No argument"
-   If only one argument is passed to the script, print "Argument found"
-   Otherwise, print "Arguments found"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

Reference: [process.argv](https://alx-intranet.hbtn.io/rltoken/5kTYi3rxb6KM1_pivm-tXg "process.argv")

```
@ubuntu:~/0x12$ ./2-arguments.js
No argument
@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
@ubuntu:~/0x12$

```

#### [3. Value of my argument](3-value_argument.js)

Write a script that prints the first argument passed to it:

-   If no arguments are passed to the script, print "No argument"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You are not allowed to use `length`

```
@ubuntu:~/0x12$ ./3-value_argument.js
No argument
@ubuntu:~/0x12$ ./3-value_argument.js School
School
@ubuntu:~/0x12$

```

#### [4. Create a sentence](4-concat.js)

Write a script that prints two arguments passed to it, in the following format: " is "

-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
@ubuntu:~/0x12$ ./4-concat.js c
c is undefined
@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
@ubuntu:~/0x12$

```

#### [5. An Integer](5-to_integer.js)

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

-   If the argument can't be converted to an integer, print "Not a number"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You are not allowed to use `try/catch`

```
@ubuntu:~/0x12$ ./5-to_integer.js
Not a number
@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
@ubuntu:~/0x12$

```

#### [6. Loop to languages](6-multi_languages_loop.js)

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

-   The first line: "C is fun"
-   The second line: "Python is cool"
-   The third line: "JavaScript is amazing"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You are not allowed to use any `if/else` statement
-   You can use only one `console.log`
-   You must use a loop (`while`, `for`, etc.)

```
@ubuntu:~/0x12$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
@ubuntu:~/0x12$

```

#### [7. I love C](7-multi_c.js)

Write a script that prints `x` times "C is fun"

-   Where `x` is the first argument of the script
-   If the first argument can't be converted to an integer, print "Missing number of occurrences"
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You can use only two `console.log`
-   You must use a loop (`while`, `for`, etc.)

```
@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
@ubuntu:~/0x12$ ./7-multi_c.js
Missing number of occurrences
@ubuntu:~/0x12$ ./7-multi_c.js -3
@ubuntu:~/0x12$

```

#### [8. Square](8-square.js)

Write a script that prints a square

-   The first argument is the size of the square
-   If the first argument can't be converted to an integer, print "Missing size"
-   You must use the character `X` to print the square
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`
-   You must use a loop (`while`, `for`, etc.)

```
@ubuntu:~/0x12$ ./8-square.js
Missing size
@ubuntu:~/0x12$ ./8-square.js School
Missing size
@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
@ubuntu:~/0x12$ ./8-square.js -3
@ubuntu:~/0x12$

```

#### [9. Add](9-add.js)

Write a script that prints the addition of 2 integers

-   The first argument is the first integer
-   The second argument is the second integer
-   You have to define a function with this prototype: `function add(a, b)`
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ ./9-add.js
NaN
@ubuntu:~/0x12$ ./9-add.js 1
NaN
@ubuntu:~/0x12$ ./9-add.js 1 7
8
@ubuntu:~/0x12$ ./9-add.js 13 89
102
@ubuntu:~/0x12$

```


#### [10. Factorial](10-factorial.js)

Write a script that computes and prints a factorial

-   The first argument is integer (argument can be cast as integer) used for computing the factorial
-   Factorial of `NaN` is `1`
-   You must do it recursively
-   You must use a function
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ ./10-factorial.js
1
@ubuntu:~/0x12$ ./10-factorial.js 3
6
@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
@ubuntu:~/0x12$

```


#### [11. Second biggest!](11-second_biggest.js)

Write a script that searches the second biggest integer in the list of arguments.

-   You can assume all arguments can be converted to integer
-   If no argument passed, print `0`
-   If the number of arguments is 1, print `0`
-   You must use `console.log(...)` to print all output
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ ./11-second_biggest.js
0
@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
@ubuntu:~/0x12$

```


#### [12. Object](12-object.js)

Update this script to replace the value `12` with `89`:

-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
@ubuntu:~/0x12$

```

#### [13. Add file](13-add.js)

Write a function that returns the addition of 2 integers.

-   The function must be visible from outside
-   The name of the function must be `add`
-   You are not allowed to use `var`

[Tip](https://alx-intranet.hbtn.io/rltoken/1k6VPdLchwtGubOfPyGL1Q "Tip")

```
@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
@ubuntu:~/0x12$ ./13-main.js
8
@ubuntu:~/0x12$

```


#### [14. Const or not const](100-let_me_const.js)

Write a file that modifies the value of `myVar` to `333`

```
@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
@ubuntu:~/0x12$ ./100-main.js
333
@ubuntu:~/0x12$

```

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/4ae30fb44f708dbb3abc211b784db614e615ca21.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220301%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220301T121514Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a1f02cfa1a04eae1b926f44e9a5b754a0ebf8e706a6b5f5be7f2445959cc4c4f)

Do you get it? Tweet! Post! Talk about it!

Hint: Scope

**This exercise doesn't pass `semistandard`** so don't worry about it.


#### [15. Call me Moby](101-call_me_moby.js)

Write a function that executes `x` times a function.

-   The function must be visible from outside
-   Prototype: `function (x, theFunction)`
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
@ubuntu:~/0x12$

```

#### [16. Add me maybe](102-add_me_maybe.js)

Write a function that increments and calls a function.

-   The function must be visible from outside
-   Prototype: `function (number, theFunction)`
-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
@ubuntu:~/0x12$ ./102-main.js
New value: 5
@ubuntu:~/0x12$

```

#### [17. Increment object](103-object_fct.js)

Update this script by adding a new function `incr` that increments the integer `value`.

-   You are not allowed to use `var`

```
@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

@ubuntu:~/0x12$ ./103-object_fct.js
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
@ubuntu:~/0x12$

```
