from pprint import pprint

RAV4 = {
    "model": "RAV4 Гібрид Lounge",
    "cost_grn": 1_807_000,
    "engine_displacement_cm": 2_487,
    "full_weight_kg": 2_135,
    "maximum_speed_km/h": 180,
    "fuel_consumption_per_hundred_km": 4.9,
    "features_of_the_interios": ['Задній підлокітник','Кермо оздоблене шкірою',
                                 'Оздоблення селектора КПП шкірою','Стеля сірого кольору'],
    "parameters_of_the_luggage_compartment": {
        "trunk_volume_l": 580,
        "trunk_space_with_seat_folded_l": 1_690,
    },
}

RAV4["Maximum_permissible_trailer_weight_with_brakes_kg"] = 800


name = RAV4["model"]
print(name)
cost = RAV4["cost_grn"]
print(cost)
features_the_interios = RAV4["features_of_the_interios"]

has_features_of_the_interios = len(features_the_interios) >= 1
if features_the_interios:
     first_features_the_interios = features_the_interios[0]
     print(first_features_the_interios)

trunk_volume_with_seats_folde = RAV4.get('parameters_of_the_luggage_compartment',{'trunk_space_with_seat_folded_l'})
print(trunk_volume_with_seats_folde)

insurance_payment = cost * 0.005
RAV4['insurance_payment'] = insurance_payment
gasoline_prices = 93
the_fuel_need = RAV4["fuel_consumption_per_hundred_km"] * 2
the_cost_of_the_trip_to_two_hundred_km = the_fuel_need * gasoline_prices
the_final_cost_of_the_trip_to_two_hundred_km = round(the_cost_of_the_trip_to_two_hundred_km)
print(the_final_cost_of_the_trip_to_two_hundred_km)
pprint(RAV4,indent=4)