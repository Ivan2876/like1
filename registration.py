import messages

name_input = input(messages.MSG_INPUT_NAME)
name = name_input.strip()
if name.isalpha():
    print(f"{messages.MSG_NAME_OK}: {name.title()}")
else:
    print(messages.MSG_NAME_ERROR)

age_input = input(messages.MSG_INPUT_AGE)
age = age_input.strip().lstrip("0")
if age.isdigit():
    print(f"{messages.MSG_AGE_OK}: {age}")
else:
    print(messages.MSG_AGE_ERROR)

phone_input = input(messages.MSG_INPUT_PHONE)
phone = phone_input.strip()
if phone.isdigit():
    print(f"{messages.MSG_PHONE_OK}:{phone}")
    print(messages.MSG_FINISH)
else:
    print(messages.MSG_PHONE_ERROR)