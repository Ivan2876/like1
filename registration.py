import messages

name_input = input(messages.MSG_INPUT_NAME)
name = name_input.strip()
if name.isalpha():
    print(messages.MSG_NAME_OK.format(name=name))
else:
    print(messages.MSG_NAME_ERROR)

age_input = input(messages.MSG_INPUT_AGE)
age = age_input.strip().lstrip("0")
if age.isdigit():
    print(messages.MSG_AGE_OK.format(age=age))
else:
    print(messages.MSG_AGE_ERROR)

phone_input = input(messages.MSG_INPUT_PHONE)
phone = phone_input.strip()
if phone.isdigit():
    print(messages.MSG_PHONE_OK.format(phone=phone))
    print(messages.MSG_FINISH)
else:
    print(messages.MSG_PHONE_ERROR)