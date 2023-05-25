from dataclasses import dataclass


@dataclass
class Subscription:
    discount: float
    minibarComplimentary: bool


DEFAULT_SUB = Subscription(discount=0.3, minibarComplimentary=True)
DEFAULT_WITHOUT_SUB = Subscription(discount=0, minibarComplimentary=False)
