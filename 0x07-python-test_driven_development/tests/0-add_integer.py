#!/usr/bin/python3
def add_integer(a, b=98):
    """function adds two integers"""
    if type(a) is int or type(b) is int:
       return (a + b)
    elif type(a) is float or type(b) is float:
        return int(a + b)
    else:
        raise TypeError("a must be an integer or b must be an integer")

