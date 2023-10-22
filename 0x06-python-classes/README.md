# *0x06. Python - Classes and Objects*

`Python`   `OOP`

By: Guillaume

![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

## *Background Context:*

OOP is a totally new concept for all of you (especially those who think they know about it :)). It’s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

## *Resources:*

Read or watch:

- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet)
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

# *General:*

- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function

## *Tasks:*

#### [0. My first square]()

Write an empty class `Square` that defines a square:

- You are not allowed to import any module

#### [1. Square with size]()

Write a class `Square` that defines a square by: (based on `0-square.py`)

- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

#### [2. Size validation]()

Write a class `Square` that defines a square by: (based on `1-square.py`)

- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
   - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
   - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are not allowed to import any module

#### [3. Area of a square]()

Write a class `Square` that defines a square by: (based on `2-square.py`)

- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
   - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
   - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

#### [4. Access and update private attribute]()

Write a class `Square` that defines a square by: (based on `3-square.py`)

- Private instance attribute: `size`:
   - property def size(self): to retrieve it
   - property setter `def size(self, value)`: to set it:
      - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
      - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional size: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

#### [5. Printing a square]()

Write a class `Square` that defines a square by: (based on `4-square.py`)

- Private instance attribute: `size`:
   - property `def size(self):` to retrieve it
   - property setter `def size(self, value):` to set it:
      - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
      - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional size: ` def __init__(self, size=0):`
- Public instance method: `def area(self)`: that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
      - if `size` is equal to 0, print an empty line
- You are not allowed to import any module

#### [6. Coordinates of a square]()

Write a class `Square` that defines a square by: (based on `5-square.py`)

- Private instance attribute: `size`:
   - property `def size(self)`: to retrieve it
   - property setter `def size(self, value)`: to set it:
      - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
      - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
   - property `def position(self)`: to retrieve it
   - property setter `def position(self, value)`: to set it:
      - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self)`: that returns the current square area
- Public instance method: `def my_print(self)`: that prints in stdout the square with the character `#`:
   - if `size` is equal to 0, print an empty line
   - `position` should be use by using space - Don’t fill lines by spaces when `position[1] > 0`
- You are not allowed to import any module

#### [7. Singly linked list]()

Write a class `Node` that defines a node of a singly linked list by:

- Private instance attribute: `data`:
   - property `def data(self)`: to retrieve it
   - property setter `def data(self, value)`: to set it:
      - `data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`
- Private instance attribute: `next_node`:
   - property `def next_node(self)`: to retrieve it
   - property setter `def next_node(self, value)`: to set it:
      - `next_node` can be `None` or must be a `Node`, otherwise raise a `TypeError` exception with the message `next_node must be a Node object`
- Instantiation with `data` and `next_node`: `def __init__(self, data, next_node=None)`:
And, write a class `SinglyLinkedList` that defines a singly linked list by:

- Private instance attribute: `head` (no setter or getter)
- Simple instantiation: `def __init__(self)`:
- Should be printable:
   - print the entire list in stdout
   - one node number by line
- Public instance method: `def sorted_insert(self, value)`: that inserts a new `Node` into the correct sorted position in the list (increasing order)
- You are not allowed to import any module

#### [8. Print Square instance]()

Write a class `Square` that defines a square by: (based on `6-square.py`)

- Private instance attribute: `size`:
   - property `def size(self)`: to retrieve it
   - property setter `def size(self, value)`: to set it:
      - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
      - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
   - property `def position(self)`: to retrieve it
   - property setter `def position(self, value)`: to set it:
      - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integer`
- Instantiation with optional `size` and optional position: `def __init__(self, size=0, position=(0, 0))`:
- Public instance method: `def area(self)`: that returns the current square area
- Public instance method: `def my_print(self)`: that prints in stdout the square with the character `#`:
   - if `size` is equal to 0, print an empty line
   - `position` should be use by using space
- Printing a `Square` instance should have the same behavior as `my_print()`
- You are not allowed to import any module

#### [9. Compare 2 squares]()

Write a class `Square` that defines a square by: (based on `4-square.py`)

- Private instance attribute: `size`:
   - property `def size(self)`: to retrieve it
   - property setter `def size(self, value)`: to set it:
      - `size` must be a number (float or integer), otherwise raise a `TypeError` exception with the message `size must be a number`
      - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with size: `def __init__(self, size=0)`:
- Public instance method: `def area(self)`: that returns the current square area
- `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area
- You are not allowed to import any module

#### [10. ByteCode -> Python #5]()

Write the Python class `MagicClass` that does exactly the same as the following Python bytecode:
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```
- Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)





