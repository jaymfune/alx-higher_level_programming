def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            # Extract elements from lists, default to 0 if lists are too short
            elem1 = my_list_1[i] if i < len(my_list_1) else 0
            elem2 = my_list_2[i] if i < len(my_list_2) else 0

            # Check if elements are numeric (integer or float)
            if not isinstance(elem1, (int, float)) or not isinstance(elem2, (int, float)):
                raise TypeError("wrong type")

            # Check if division by 0
            if elem2 == 0:
                raise ZeroDivisionError("division by 0")

            # Perform division and append result to the result_list
            result_list.append(elem1 / elem2)

    except TypeError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: out of range")
    finally:
        return result_list