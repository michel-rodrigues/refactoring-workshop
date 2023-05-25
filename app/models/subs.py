from dataclasses import dataclass


@dataclass
class Subscription:
    discount: float
    minibarComplimentary: bool
    breakfastComplimentary: bool


PLATINUM_SUB = Subscription(discount=0.45, minibarComplimentary=True, breakfastComplimentary=True)
GOLD_SUB = Subscription(discount=0.3, minibarComplimentary=True, breakfastComplimentary=False)
FREE_SUB = Subscription(discount=0, minibarComplimentary=False, breakfastComplimentary=False)
