

def average(numbner1, numbner2, numbner3,arguments_number) -> int | float:
    average_value = numbner1 +numbner2 + numbner3
    average_value = average_value / arguments_number
    average_value = round(average_value, 2)
    return average_value
average_value2 = average(numbner1=100, numbner2=2,numbner3=3,arguments_number=3)
print(average_value2)

def foo(something) -> bool:
    if something > 10 and something % 2 == 0:
        return True
    else:
        return False
the_number_is_even_and_greater_than_ten = foo(something=16)
print(the_number_is_even_and_greater_than_ten)
the_number_is_even_and_greater_than_ten_wrong = foo(something=15)
print(the_number_is_even_and_greater_than_ten_wrong)


def vowels(text: str,) -> int:
    wabls = "aeiouy"
    text = text.lower()
    counter = 0
    for letter in text:
        if letter in wabls:
            counter += 1
    return counter

get_many_vowels_are_there_in_a_row = vowels('aeiou')
print(get_many_vowels_are_there_in_a_row)