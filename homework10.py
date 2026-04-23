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
needs_tempreg = "190°C"
which_foods_are_cooked_at_what_temperature_190 = []
the_most_caloric_dish = 0
the_most_caloric_dish_name = ""
how_many_views_have_there_been_for_all_recipes = 0

for recipe in recipes:
    instructions = recipe['instructions']
    cuisine = recipe['cuisine']
    caloriesPerServing = recipe['caloriesPerServing']
    if caloriesPerServing > the_most_caloric_dish:
        the_most_caloric_dish = caloriesPerServing
        the_most_caloric_dish_name = recipe['name']
        reviewCount = recipe['reviewCount']
        how_many_views_have_there_been_for_all_recipes += reviewCount

    if needs_tempreg in instructions[0]:
        which_foods_are_cooked_at_what_temperature_190.append(recipe)
    if search_text in cuisine:
        how_many_dishes_belong_to_Italian_cuisine.append(cuisine)

pprint(which_foods_are_cooked_at_what_temperature_190)
print(the_most_caloric_dish, the_most_caloric_dish_name,'-найбільш калорійна їжа')
print(how_many_dishes_belong_to_Italian_cuisine.count('Italian'),'-скільки страв відносяться до італійської кухні')
print(how_many_views_have_there_been_for_all_recipes, '-скільки всього було переглядів всіх рецептів')