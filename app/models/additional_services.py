from dataclasses import dataclass
from app.models.subs import Subscription


@dataclass
class AdditionalService:
    name: str
    base_price: int

    def get_fee(self, subscription: Subscription):
        return self.base_price


class Breakfast(AdditionalService):
    def get_fee(self, subscription: Subscription):
        return self.base_price if not subscription.breakfastComplimentary else 0


MASSAGE = AdditionalService(name="massage", base_price=12000)
SAUNA = AdditionalService(name="sauna", base_price=3000)
BREAKFAST = Breakfast(name="breakfast", base_price=2500)
