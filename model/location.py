from dataclasses import dataclass


@dataclass
class Location:
    loc: str
    lat: float
    long: float