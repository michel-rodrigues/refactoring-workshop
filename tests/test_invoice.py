from app.hotel import calculateInvoice
from app.models.stay_informations import StayInformations
from app.models.subs import GOLD_SUB, FREE_SUB, PLATINUM_SUB
from app.rooms import PRESIDENTIAL_ROOM, DELUXE_ROOM, STANDARD_ROOM

## 25/05/2023 > falta add teste de massagem e massagem + sauna

def test_calculate_presidential_invoice_with_sauna():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'breakfast': 0,
        'total': 26418,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=2,
            state='SP',
            subscription=GOLD_SUB,
            room=PRESIDENTIAL_ROOM,
            minibarConsumed=True,
            breakfastAdded=False,
            massageAdded=False,
            saunaAdded=True
        )
    )
    assert invoice == expected_invoice

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
            subscription=GOLD_SUB,
            room=PRESIDENTIAL_ROOM,
            minibarConsumed=True,
            breakfastAdded=False,
            massageAdded=False,
            saunaAdded=False
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
            subscription=FREE_SUB,
            room=DELUXE_ROOM,
            minibarConsumed=True,
            breakfastAdded=True,
            massageAdded=False,
            saunaAdded=False
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
            subscription=FREE_SUB,
            room=STANDARD_ROOM,
            minibarConsumed=False,
            breakfastAdded=True,
            massageAdded=False,
            saunaAdded=False
        )
    )
    assert invoice == expected_invoice


def test_calculate_standard_invoice_when_platinum_subscription():
    expected_invoice = {
        'roomPrice': 36000,
        'minibar': 0,
        'breakfast': 0,
        'total': 20394,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=4,
            state='RJ',
            subscription=PLATINUM_SUB,
            room=STANDARD_ROOM,
            minibarConsumed=False,
            breakfastAdded=True,
            massageAdded=False,
            saunaAdded=False
        )
    )
    assert invoice == expected_invoice
