from vehicle import Vehicle
import exceptions


class Plane(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo:float = 0
        self.max_cargo:float = 0

    def load_cargo(self, cargo:float) -> None:
        if cargo + self.cargo > self.max_cargo:
            raise exceptions.CargoOverload

        self.cargo += cargo

    def remove_all_cargo(self) ->float:
        cargo = self.cargo
        self.cargo = 0
        return cargo
