from dataclasses import dataclass

from app.models.subs import Subscription
from app.rooms import Room


@dataclass
class StayInformations:
    nights: int
    room: Room
    subscription: Subscription
    state: str
    minibarConsumed: bool
    breakfastAdded: bool
    massageAdded: bool
    saunaAdded: bool
    services: list = []

    def calculate_total_amount(self):
        total_amount = (
                       self.calculate_room_price() +
                       self.calculate_minibar_fee() +
                       self.calculate_breakfast_fee() +
                       self.calculate_massage_fee() +
                       self.calculate_sauna_fee()
               ) * (1 - self.subscription.discount)
        return round(total_amount)

    def calculate_room_price(self):
        return self.room.price * self.nights

    def calculate_minibar_fee(self):
        return self.room.minibarFee if self.minibarConsumed and not self.subscription.minibarComplimentary else 0

    def calculate_breakfast_fee(self):
        return 2500 if self.breakfastAdded and not self.subscription.breakfastComplimentary else 0

    def calculate_massage_fee(self):
        return 12000 if self.massageAdded else 0

    def calculate_sauna_fee(self):
        return 3000 if self.saunaAdded else 0
