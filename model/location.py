from dataclasses import dataclass


@dataclass
class Location:
    loc: str
    lat: float
    long: float



    def __hash__(self):
        return hash(self.loc)

    def __str__(self):
        return self.loc