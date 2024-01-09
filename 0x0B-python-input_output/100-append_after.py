#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string."""
    if not filename or not search_string or not new_string:
        return

    with open(filename, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)
