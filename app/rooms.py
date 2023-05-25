from dataclasses import dataclass


@dataclass
class Room:
    type: str
    price: int
    hasHotTub: bool
    minibarFee: int


STANDARD_ROOM = Room(type="standard", price=9000, hasHotTub=False, minibarFee=0)
DELUXE_ROOM = Room(type="deluxe", price=14000, hasHotTub=False, minibarFee=7500)
PRESIDENTIAL_ROOM = Room(type="presidential", price=17000, hasHotTub=True, minibarFee=9500)
