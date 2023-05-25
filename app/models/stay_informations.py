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

    def calculate_total_amount(self):
        return (
            self.calculate_room_price() +
            self.calculate_minibar_fee() +
            self.calculate_breakfast_fee()
        ) * (1 - self.subscription.discount)

    def calculate_room_price(self):
        return self.room.price * self.nights

    def calculate_minibar_fee(self):
        return self.room.minibarFee if self.minibarConsumed and not self.subscription.minibarComplimentary else 0

    def calculate_breakfast_fee(self):
        return 2500 if self.breakfastAdded else 0
