## *0x09. Python - Everything is object*

`Python`   `OOP`

By: Guillaume

![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

## *Background Context*

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
``` 
OK. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```


This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.

## *Resources:*

Read or watch:

- [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation](https://www.composingprograms.com/pages/24-mutable-data.html) (Only this chapter)
- [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)

## *General:*

- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## *Tasks:*

#### [0. Who am I?]()

What function would you use to get the type of an object?

Write the name of the function in the file, without `()`.

#### [1. Where are you?]()

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

#### [2. Right count]()

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

#### [3. Right count =]()

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

#### [4. Right count =]()

In the following code, do `a` and `b` point to the same object? Answer with `Yes` or `No`.

#### [5. Right count =+]()

In the following code, do a and b point to the same object? Answer with Yes or No.
```
>>> a = 89
>>> b = a + 1
```

#### [6. Is equal]()

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

#### [7. Is the same]()

What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

#### [8. Is really equal]()

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

#### [9. Is really the same]()

What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

#### [10. And with a list, is it equal]()

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

#### [11. And with a list, is it the same]()

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

#### [12. And with a list, is it really equal]()

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

#### [13. And with a list, is it really the same]()

What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
#### [14. List append]()

What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
#### [15. List add]()

What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
#### [16. Integer incrementation]()

What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
#### [17. List incrementation]()

What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
#### [18. List assignation]()

What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
#### [19. Copy a list object]()

Write a function `def copy_list(l):` that returns a copy of a list.

- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module

#### [20. Tuple or not?]()
```
a = ()
```
Is `a` a tuple? Answer with `Yes` or `No`.

#### [21. Tuple or not?]()
```
a = (1, 2)
```
Is `a` a tuple? Answer with `Yes` or `No`.

#### [22. Tuple or not?]()
```
a = (1)
```
Is `a` a tuple? Answer with `Yes` or `No`.

#### [23. Tuple or not?]()
```
a = (1, )
```
Is `a` a tuple? Answer with `Yes` or `No`.

#### [24. Who I am?]()

What does this script print?
```
a = (1)
b = (1)
a is b
```
#### [25. Tuple or not]()

What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```

#### [26. Empty is not empty]()

What does this script print?
```
a = ()
b = ()
a is b
```

#### [27. Still the same?]()
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

#### [28. Same or not?]()
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

#### [29. #pythonic]()

Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration (see code):

- Format: see example
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module
- Format example:
```
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())
```
#### [30. Low memory cost]()
 
Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.

- You are not allowed to import any module

#### [31. int 1/3]()
```
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)
- How many int objects are created by the execution of the second line of the script (`103-line2.txt`)

#### [32. int 2/3]()
```
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
- How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
- After the execution of line 3, is the int object pointed by `a` deleted? Answer with `Yes` or `No` (`104-line3.txt`)
- After the execution of line 4, is the int object pointed by `b` deleted? Answer with `Yes` or `No` (`104-line4.txt`)
- How many int objects are created by the execution of the last line of the script (`104-line5.txt`)

#### [33. int 3/3]()
```
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:

- Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? (`105-line1.txt`)
- Why? (optional blog post :))
Hint: `NSMALLPOSINTS`, `NSMALLNEGINTS`

![4p9p4o](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/70f9ea0e969dfcc407a7427aba4786d87a920494.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231023%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231023T204334Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=506d56d5691383942e19e48d4522161664d7a7b61ec6e8745405b991f723bdc5)

#### [34. Clear strings]()
```
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

- How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
- How many string objects are created by the execution of the second line of the script (`106-line2.txt`)
- After the execution of line 3, is the string object pointed by `a` deleted? Answer with `Yes` or `No` (`106-line3.txt`)
- After the execution of line 4, is the string object pointed by `b` deleted? Answer with `Yes` or `No` (`106-line4.txt`)
- How many string objects are created by the execution of the last line of the script (`106-line5.txt`)


















