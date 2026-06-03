class Car:
    def __init__(self,model: str,age: int,owner: str =None, fuel: int = 0,):
        self.unique_car_identifier = id(self)
        self.fuel = fuel
        self.age = age
        self.owner = owner
        self.model= model
    def __str__(self) -> str:
        return (f"model = {self.model}, age = {self.age}, owner = {self.owner},"
                f" fuel = {self.fuel},car_identifier = {self.unique_car_identifier}")

    def add_amount_of_gasoline(self, add_fuel: int) -> int:
        self.fuel += add_fuel

    @property
    def get_car_age(self) -> str:
        if self.age <= 3:
            return"нове авто"
        if self.age <= 6:
            return"середній стан"
        return "старе авто"


    @property
    def get_if_enough_gas(self) -> str:
        if self.fuel > 15:
            return "Достатньо бензину"
        else:
            return "Потрібна заправка"


car1 = Car(model="BMW", age=3,owner="Alex",fuel=75)
car2 = Car(model="Mercedes",age=6,fuel=80)

print(id(car1))
print(id(car2))
print(car1.__dict__)
print(car2.__dict__)
print(car1)
print(car2)
car1.fuel += 10
print(car1.__dict__)
car2.add_amount_of_gasoline(13)
print(car2.__dict__)
machine_condition1 = car1.get_car_age
machine_condition2 = car2.get_car_age
print(machine_condition1)
print(machine_condition2)
true_or_false = car1.fuel > car2.fuel
print(true_or_false)
car1.fuel -= 75
need_required1 = car1.get_if_enough_gas
need_required2 = car2.get_if_enough_gas
print(need_required1)
print(need_required2)
