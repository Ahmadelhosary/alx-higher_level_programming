#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for let in range(97, 123):
    if let != 101 and let != 113:
        print("{}".format(chr(let)), end="")
