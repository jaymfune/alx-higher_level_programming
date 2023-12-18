#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count_integers = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                count_integers += 1
        print()
        return count_integers
    except IndexError:
        return count_integers