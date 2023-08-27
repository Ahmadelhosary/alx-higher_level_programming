#!/usr/bin/python3
"""program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase"""

for code in range(122, 96, -1):
    print("{}{}".format(chr(code), chr(code - 32)), end="")
