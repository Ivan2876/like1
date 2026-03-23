import messages
from messages import MSG_INPUT_WATER_NUMBER


water_number = input(messages.MSG_INPUT_WATER_NUMBER).strip().lstrip("0")
print(water_number)

is_correct_water_number = water_number.isdigit()
print(is_correct_water_number)
true = True
false = False

if is_correct_water_number:
    print(messages.MSG_CORRECT_INPUT)
else:
    print(messages.MSG_INCORRECT_INPUT)

# is_only_letters = water_number.isalpha()
# print(is_only_letters)

# is_only_ascii = water_number.isascii()
# print(is_only_ascii)

is_lower = water_number.islower()
print(is_lower)



print(messages.MSG_FINISH)

