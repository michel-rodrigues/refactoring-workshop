from app.hotel import calculateInvoice
from app.models.stay_informations import StayInformations
from app.models.subs import DEFAULT_SUB, DEFAULT_WITHOUT_SUB
from app.rooms import PRESIDENTIAL_ROOM, DELUXE_ROOM, STANDARD_ROOM


def test_calculate_presidential_invoice():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'breakfast': 0,
        'total': 24276,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=2,
            state='SP',
            subscription=DEFAULT_SUB,
            room=PRESIDENTIAL_ROOM,
            minibarConsumed=True,
            breakfastAdded=False,
        )
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
        StayInformations(
            nights=3,
            state='SP',
            subscription=DEFAULT_WITHOUT_SUB,
            room=DELUXE_ROOM,
            minibarConsumed=True,
            breakfastAdded=True,
        )
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
        StayInformations(
            nights=4,
            state='RJ',
            subscription=DEFAULT_WITHOUT_SUB,
            room=STANDARD_ROOM,
            minibarConsumed=False,
            breakfastAdded=True,
        )
    )
    assert invoice == expected_invoice
