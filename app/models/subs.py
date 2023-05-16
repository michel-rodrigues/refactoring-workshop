
from dataclasses import dataclass

@dataclass
class Subscriber:
  discount: float
  minibarComplimentary: bool

DEFAULT_SUB = Subscriber(discount=0.3, minibarComplimentary=True)
DEFAULT_WITHOUT_SUB = Subscriber(discount=0, minibarComplimentary=False)