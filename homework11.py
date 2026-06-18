import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycbxZ4Kq38WtZ6DRhkb_w5u3MfZr_X11pXt67tkTM1y3bR_HxLWIfe_p2_ael9bVVYoCSLg/exec'
response = requests.get(url=url, params={})
response_json = response.json()

pprint(response_json)
animals = response_json['animals']
the_cost_of_caring_for_poisonous_animals = 0
how_many_African_animals_are_currently_in_the_zoo = 0


for animal in animals:
    care_cost = animal['Care_cost']
    count = animal['Count']
    if 'африка' == animal['Continent'].lower():
        how_many_African_animals_are_currently_in_the_zoo += count
    if 'так' in animal['Is_venomous'].lower():
        the_cost_of_caring_for_poisonous_animals += care_cost * count


print(how_many_African_animals_are_currently_in_the_zoo,'-скільки африканських тварин наразі в зоопарку')
print(the_cost_of_caring_for_poisonous_animals,'-вартість догляду за отруйними тваринами')


