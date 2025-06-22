#!/usr/bin/python3
print("".join("{}{}".format(chr(i), chr(i - 33)) for i in range(122, 96, -2)), end="")
