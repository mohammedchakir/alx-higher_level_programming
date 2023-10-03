#!/usr/bin/python3
for Alph in range(122, 96, -1):
    if Alph % 2:
        Alph = Alph - 32
    print("{:c}".format(Alph), end="")
