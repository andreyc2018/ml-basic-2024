from dataclasses import dataclass


@dataclass
class Engine:
    """Class for keeping track of an item in inventory."""
    volume: float = 0
    pistons: int = 0
