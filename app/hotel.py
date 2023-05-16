from app.rooms import Room
from app.subscriber import Subscriber

STATES_TAX = {"SP": 0.02, "RJ": 0.03}


def calculate_invoice(
        nights: int,
        room: Room,
        state: str,
        subscriber: Subscriber,
        minibar_consumed: bool,
        breakfast_added: bool
):

    # Pensamos que ainda podemos refatorar a parte das taxas para controlar as responsabilidades do metodo
    room_price = room.calculate_room_price(nights)
    minibar_fee = room.minibarFee if minibar_consumed and not subscriber.minibarCourtesy else 0
    breakfast_fee = subscriber.breakfastTax if breakfast_added else 0

    total = get_total(room_price, minibar_fee, breakfast_fee, state, subscriber)

    return {
        'roomPrice': room_price,
        'minibar': minibar_fee,
        'breakfast': breakfast_fee,
        'total': total
    }


def get_total(room_price, minibar_fee, breakfast_fee, state, subscriber):
    total = room_price + minibar_fee + breakfast_fee
    total -= total * subscriber.totalDiscount

    total_with_tax = get_state_tax(state, total)

    return total_with_tax


def get_state_tax(state: str, total: float) -> float:
    total += total * STATES_TAX[state]
    return total
