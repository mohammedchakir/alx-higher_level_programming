#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
result1 = add(a, b)
result2 = sub(a, b)
result3 = mul(a, b)
result4 = div(a, b)

print(f"{a} + {b} = {result1}")
print(f"{a} - {b} = {result2}")
print(f"{a} * {b} = {result3}")
print(f"{a} / {b} = {result4}")
