from abc import ABC, abstractmethod
from typing import Self

class Transport(ABC):
    def __init__(self, fuel: int, condition: int):
        self.fuel = fuel
        self.condition = condition
    @property
    def is_working (self):
        return self.condition > 10

    @abstractmethod
    def __str__(self) -> str:
        return ''

    def move (self,distance):
        if not self.fuel > 0 and not self.condition > 10:
            return print("рух неможливий")

        if self.fuel > 0 and self.condition > 10:
            self.fuel -= distance / 3
            self.condition -= distance / 9
            return (f"ви проїхали {distance} кілометрів"
            and print(self))

class Car(Transport):
    def __init__(self, model: str,fuel: int = 50, condition: int = 100,):
        super().__init__(fuel, condition)
        self.model = model
    def get_info(self):
        return (f"у транспорті є {self.fuwel} літрів пального, його стан {self.condition} зі 100, і його модель: {self.model}")


class Truck(Transport):
    def __init__(self, model: str,fuel: int = 120, condition: int = 100,):
        super().__init__(fuel, condition)
        self.model = model
    def get_info(self):
            return (f"у транспорті є {self.fuel} літрів пального, його стан {self.condition} зі 100, і його модель: {self.model}")


class Motorcycle(Transport):
    def __init__(self, model: str):
        super().__init__(fuel = 20, condition= 100)
        self.model = model
    def get_info(self):
        return (f"у транспорті є {self.fuel} літрів пального, його стан {self.condition} зі 100, і його модель: {self.model}")



car = Car
truck = Truck
motorcycle = Motorcycle

