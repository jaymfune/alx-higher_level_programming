#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    try:
        if my_list is None:
            my_list = []
        for i in range(min(x, len(my_list))):
            print(my_list[i], end="")
        print()
        return x
    except IndexError:
        return i
