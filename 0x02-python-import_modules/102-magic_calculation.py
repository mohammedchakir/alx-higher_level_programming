#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        add = __import__('magic_calculation_102').add
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return (c)
    else:
        sub = __import__('magic_calculation_102').sub
        return sub(a, b)
