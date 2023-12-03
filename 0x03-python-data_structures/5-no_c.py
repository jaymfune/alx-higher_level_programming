#!/usr/bin/python3
def no_c(str):
    new_str = str.translate({ord(i): None for i in 'cC'})
    return new_str
