#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            elem1 = my_list_1[i]
            elem2 = my_list_2[i]
            if not (isinstance(elem1, (int, float)) and
                    isinstance(elem2, (int, float))):
                print("wrong type")
                raise TypeError
            if elem2 == 0:
                print("division by 0")
                raise ZeroDivisionError
            division = elem1 / elem2
        except IndexError:
            print("out of range")
            division = 0
        except (TypeError, ZeroDivisionError):
            division = 0
        finally:
            result.append(division)
    return result
