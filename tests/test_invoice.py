from app.hotel import calculateInvoice
from app.rooms import PRESIDENTIAL_ROOM, DELUXE_ROOM, STANDARD_ROOM

def test_calculate_presidential_invoice():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'breakfast': 0,
        'total': 24276,
    }
    invoice = calculateInvoice(
        nights=2,
        state='SP',
        room=PRESIDENTIAL_ROOM,
        isSubscriber=True,
        minibarConsumed=True,
        breakfastAdded=False,
    )
    assert invoice == expected_invoice


def test_calculate_deluxe_invoice():
    expected_invoice = {
        'roomPrice': 42000,
        'minibar': 7500,
        'breakfast': 2500,
        'total': 53040,
    }
    invoice = calculateInvoice(
        nights=3,
        state='SP',
        room=DELUXE_ROOM,
        isSubscriber=False,
        minibarConsumed=True,
        breakfastAdded=True,
    )
    assert invoice == expected_invoice


def test_calculate_standard_invoice():
    expected_invoice = {
        'roomPrice': 36000,
        'minibar': 0,
        'breakfast': 2500,
        'total': 39655,
    }
    invoice = calculateInvoice(
        nights=4,
        state='RJ',
        room=STANDARD_ROOM,
        isSubscriber=False,
        minibarConsumed=False,
        breakfastAdded=True,
    )
    assert invoice == expected_invoice