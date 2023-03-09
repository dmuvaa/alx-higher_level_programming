#!/usr/bin/python3
num = 1
while num < 100:
    if num < 10:
        new_num = "0{}, ".format(str(num))
    elif num < 99:
        new_num = "{}, ".format(str(num))
    else:
        new_num = "{}".format(str(num))
        print("{}".format(new_num), end="")

    num += 1
