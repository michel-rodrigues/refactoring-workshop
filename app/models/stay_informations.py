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
    services: list

    def calculate_total_amount(self):
        total_amount = (
                       self.calculate_room_price() +
                       self.calculate_services_fee()
               ) * (1 - self.subscription.discount)
        return round(total_amount)

    def calculate_room_price(self):
        return self.room.price * self.nights

    def calculate_services_fee(self):
        additional_services_fee = sum([service.get_fee(self.subscription) for service in self.services])
        return self.calculate_minibar_fee() + additional_services_fee

    def calculate_minibar_fee(self):
        return self.room.minibarFee if self.minibarConsumed and not self.subscription.minibarComplimentary else 0

    def additional_services_fee(self):
        return {service.name: service.get_fee(self.subscription) for service in self.services}

