from dataclasses import dataclass
from app.rooms import Room

@dataclass
class InputData:
  nights: int
  room: Room
  state: str
  isSubscriber: bool
  minibarConsumed: bool
  breakfastAdded: bool