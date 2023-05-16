class Room:
    type: str
    price: float = 9000
    hasHotTub: bool = False
    minibarFee: float = 0

    def calculate_room_price(self, nights: int) -> float:
        return self.price * nights


class StandardRoom(Room):
    def __init__(self):
        self.type = "standard"


class DeluxeRoom(Room):
    def __init__(self):
        self.type = "deluxe"
        self.minibarFee = 7500
        self.price = 14000


class PresidentialRoom(Room):
    def __init__(self):
        self.type = "presidential"
        self.minibarFee = 9500
        self.hasHotTub = True
        self.price = 17000

