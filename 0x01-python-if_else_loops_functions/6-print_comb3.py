#!/usr/bin/python3
for x in range (0, 10):
    for y in range(0, 10):
        if x != y and x < y:
            z = str(x) + str(y)
            print("{}, ".format(z), end="")
print()
