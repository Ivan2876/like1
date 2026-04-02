from asyncio.sslproto import add_flowcontrol_defaults

import letter

name_input = input(letter.NAME)
name = name_input.strip()
if name.isalpha():
    print(letter.NAME_OK.format(name=name))
else:
    print(letter.NAME_ERROR)

date_input = input(letter.DATE)
date = date_input.strip()
if date.isdigit():
    print(letter.DATE_OK.format(date=date))
else:
    print(letter.DATE_ERROR)

person_input = input(letter.PERSON)
persons = person_input.strip()
if persons.isdigit():
    print(letter.PERSON_OK.format(persons=persons))
else:
    print(letter.PERSON_ERROR)

cost_one_person = 15000
person_number = person_input.strip()

total_count = cost_one_person * int(person_number)
print(f"{total_count}")

DISCOUNT_PERCENTAGE = 0.05
DISCOUNT_TRIGER_SUME = 5

discount = 0
if int(person_number) > DISCOUNT_TRIGER_SUME:
    discount = int(total_count * DISCOUNT_PERCENTAGE)

total_price=total_count - discount

print(letter.LETTER_TEMPLATE.format(name=name,date=date,persons=persons,price_per_person=cost_one_person,total_price=total_price,discount=discount,final_price=total_price))