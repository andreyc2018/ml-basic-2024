from vehicle import Vehicle
from engine import Engine

class Car(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float) -> None:
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine:Engine) -> None:
        self.engine = engine
