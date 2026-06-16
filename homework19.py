from typing import Callable


def checks_result_of_the_function_is_an_integer(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, int):
            return result + 10

        return result
    return wrapper

def add_numbers(number_1: float, number_2: float):
    suma = number_1 + number_2
    return suma

@checks_result_of_the_function_is_an_integer
def add_numbers2(number_1: float, number_2: float):
    suma = number_1 + number_2
    return suma


try1 =add_numbers(5, number_2=3)
try2 =add_numbers(1.4,number_2=3.5)
print(try1, "before")
print(try2, 'before')

try3 =add_numbers2(5, number_2=3)
try4 =add_numbers2(1.4, number_2=3.5)
print(try3,"after")
print(try4,"after")