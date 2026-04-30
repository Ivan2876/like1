from utils import get_travel_info




# message0105 = get_travel_info(driver='Vasyl', passenger_3='Alla', passenger_2='Andriy')
# print(message0105)

message0105 = get_travel_info('Vasyl', 'alla', passenger_3='pavlo', passenger_2='petro')
print(message0105)
message0105 = get_travel_info('Vasyl', 'alla', passenger_3='petro')
print(message0105)

# message0105 = get_travel_info(passenger_3='petro')
# print(message0105)

driver, passenger_1,  *other = "vasyl", 'alla', 'pavlo', 'petro'
print(driver)
print(passenger_1)
print(other)



message3004 = get_travel_info(passenger_2='Alla', passenger_1='Andriy', passenger_3='Pavlo', driver='Vasyl')
print(message3004)

people = {
    "passenger_1": 'Nicol',
    "passenger_2": 'Nicol2',
    "driver": 'Ivan',
}

new_way_arguments_provided = get_travel_info(**people)
print(new_way_arguments_provided)


# TEMPLATE_STR = 'Our driver today is {}, and passenger {}'
# msg = TEMPLATE_STR.format(*other)
# print(msg)

TEMPLATE_STR = 'Our driver today is {driver}, and passenger {passenger_1}'
msg = TEMPLATE_STR.format(**people)
print(msg)
test_func = get_travel_info('Vadym', "Anastasiia")
print(test_func)