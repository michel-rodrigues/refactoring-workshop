from typing import Dict

from app.rooms import Room
from app.subscriber import Subscriber


class Invoice:
    nights: int
    room: Room
    subscriber: Subscriber
    services: Dict[str, bool]

    def __init__(self, nights: int, room: Room, subscriber: Subscriber, services: Dict[str, bool]):
        self.nights = nights
        self.room = room
        self.subscriber = subscriber
        self.services = services
