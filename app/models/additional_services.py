from dataclasses import dataclass


@dataclass
class AdditionalService:
    name: str
    price: int


MASSAGE = AdditionalService(name="massage", price=12000)
SAUNA = AdditionalService(name="sauna", price=3000)
BREAKFAST = AdditionalService(name="breakfast", price=2500)
