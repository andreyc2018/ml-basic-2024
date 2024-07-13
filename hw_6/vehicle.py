from abc import ABC

import exceptions


class Vehicle(ABC):
    def __init__(self, weight:float, fuel:float, fuel_consumption:float) -> None:
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self) -> None:
        if self.started:
            return

        if self.fuel <= 0:
            raise exceptions.LowFuelError

        self.started = True

    def move(self, distance:float) -> None:
        if not self.started:
            return

        if distance * self.fuel_consumption > self.fuel:
            raise exceptions.NotEnoughFuel

        self.fuel -= distance * self.fuel_consumption
