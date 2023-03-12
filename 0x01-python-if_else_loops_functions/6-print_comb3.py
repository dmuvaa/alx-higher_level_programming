#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x+1, 10):
        z = str(x) + str(y)
        if y == 9 and x == 8:
            print(z, end="")
        else:
            print("{}, ".format(z), end="")
print("\n", end="")
