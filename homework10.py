import requests
from pprint import pprint

url = 'https://dummyjson.com/recipes'
params = {
    "skip": 0,
    "limit": 1000,
}
response = requests.get(url=url ,params=params)
response_json = response.json()
recipes = response_json['recipes']
search_text = 'Italian'
how_many_dishes_belong_to_Italian_cuisine = []
needs_tempreg = 190
which_foods_are_cooked_at_what_temperature_190 = []
the_most_caloric_dish = 0
the_most_caloric_dish_name = ""
for recipe in recipes:
    instructions = recipe['instructions']
    cuisine = recipe['cuisine']
    caloriesPerServing = recipe['caloriesPerServing']
    if caloriesPerServing > the_most_caloric_dish:
        the_most_caloric_dish = caloriesPerServing
        the_most_caloric_dish_name = recipe['name']

    if needs_tempreg == instructions:
        which_foods_are_cooked_at_what_temperature_190.append(instructions)




    if search_text in cuisine:
        how_many_dishes_belong_to_Italian_cuisine.append(cuisine)


print(the_most_caloric_dish, the_most_caloric_dish_name,'-найбільш калорійна їжа')
print(which_foods_are_cooked_at_what_temperature_190,'-страви які готуються при 190 градусів')
print(how_many_dishes_belong_to_Italian_cuisine.count('Italian'),'-скільки страв відносяться до італійської кухні')
