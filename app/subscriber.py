class Subscriber:
    minibarCourtesy: bool = True
    totalDiscount: float = 0.30
    breakfastTax: float = 2500


class GoldSubscriber(Subscriber):
    pass


class PlatinumSubscriber(Subscriber):
    def __init__(self):
        self.totalDiscount = 0.45
        self.breakfastTax = 0


class NonSubscriber(Subscriber):
    def __init__(self):
        self.minibarCourtesy = False
        self.totalDiscount = 0
        self.breakfastTax = 2500
