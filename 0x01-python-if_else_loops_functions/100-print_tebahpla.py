#!/usr/bin/python3

for code in range(122, 96, -1):
    print("{}{}".format(chr(code), chr(code - 32)), end="")
