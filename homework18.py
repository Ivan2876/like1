from abc import ABC, abstractmethod
from typing import Self


class Transport(ABC):
    def __init__(self, fuel: int, condition: int):
        self.fuel = fuel
        self.condition = condition

    @property
    def is_working(self):
        return self.condition > 5

    @abstractmethod
    def __str__(self) -> str:
        return ''

    def move(self, distance):
        if not self.fuel > 0 or not self.condition > 10:
            return print("рух неможливий")

        if self.fuel > 0 and self.condition > 10:
            self.fuel -= round(distance / 2)
            self.condition -= round(distance / 6)
            return print(
                f"ви проїхали {distance} кілометрів,і в вас залишилося {self.fuel} літрів пального і стан транспорту {self.condition} зі 100")


class ServiceStation:
    def repair(self, transport_unit: Transport):
        condition_max = 100
        transport_unit.condition = condition_max


class Car(Transport):
    def __init__(self, model: str, fuel: int = 50, condition: int = 100, ):
        super().__init__(fuel, condition)
        self.model = model

    def __str__(self):
        return print(
            f"у транспорті є {self.fuel} літрів пального, його стан {self.condition} зі 100, і його модель: {self.model}")


class Truck(Transport):
    def __init__(self, model: str, fuel: int = 120, condition: int = 100):
        super().__init__(fuel, condition)
        self.model = model

    def __str__(self):
        return print(
            f"у транспорті є {self.fuel} літрів пального, його стан {self.condition} зі 100, і його модель: {self.model}")


class Motorcycle(Transport):
    def __init__(self, model: str, fuel: int = 20, condition: int = 100):
        super().__init__(fuel, condition)
        self.model = model

    def __str__(self):
        return print(
            f"у транспорті є {self.fuel} літрів пального, його стан {self.condition} зі 100, і його модель: {self.model}")


car = Car(model="BMW")
truck = Truck(model="Ford")
motorcycle = Motorcycle(model="Kugoo")
car.move(distance=50)
car.move(distance=20)
truck_is_working = truck.is_working
print(truck_is_working)
print(motorcycle.__dict__)
car2 = Car(model="BMW", fuel=0)
car2.move(distance=50)
truck2 = Truck(model="Ford", condition=0)
truck2.move(distance=20)
truck2_is_working = truck2.is_working
print(truck2_is_working)
motorcycle2 = Motorcycle(model="Kugoo", condition=20)
print(motorcycle2.__dict__, "ремонт повністю зламаного транспорту")
serviceStation = ServiceStation()
serviceStation.repair(motorcycle2)
print(motorcycle2.__dict__, "ремонт повністю зламаного транспорту")
print(motorcycle.__dict__, "ремонт працюючого транспорту")
serviceStation.repair(motorcycle)
print(motorcycle.__dict__, "ремонт працюючого транспорту")

print(motorcycle.__dict__, 'кілька ремонтів поспіль')
serviceStation.repair(motorcycle)
serviceStation.repair(motorcycle)
serviceStation.repair(motorcycle)
serviceStation.repair(motorcycle)
print(motorcycle.__dict__, "кілька ремонтів поспіль")
