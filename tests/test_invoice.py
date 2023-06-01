from app.hotel import calculateInvoice
from app.models.stay_informations import StayInformations
from app.models.subs import GOLD_SUB, FREE_SUB, PLATINUM_SUB
from app.rooms import PRESIDENTIAL_ROOM, DELUXE_ROOM, STANDARD_ROOM
from app.models.additional_services import MASSAGE, SAUNA, BREAKFAST


def test_calculate_presidential_invoice_with_massagem_and_sauna():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'massage': 12000,
        'sauna': 3000,
        'total': 34986,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=2,
            state='SP',
            subscription=GOLD_SUB,
            room=PRESIDENTIAL_ROOM,
            services=[MASSAGE, SAUNA],
            minibarConsumed=True,
        )
    )
    assert invoice == expected_invoice


def test_calculate_presidential_invoice_with_massagem():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'massage': 12000,
        'total': 32844,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=2,
            state='SP',
            subscription=GOLD_SUB,
            room=PRESIDENTIAL_ROOM,
            services=[MASSAGE],
            minibarConsumed=True,
        )
    )
    assert invoice == expected_invoice


def test_calculate_presidential_invoice_with_sauna():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'sauna': 3000,
        'total': 26418,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=2,
            state='SP',
            subscription=GOLD_SUB,
            room=PRESIDENTIAL_ROOM,
            services=[SAUNA],
            minibarConsumed=True,
        )
    )
    assert invoice == expected_invoice


def test_calculate_presidential_invoice():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'total': 24276,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=2,
            state='SP',
            subscription=GOLD_SUB,
            room=PRESIDENTIAL_ROOM,
            services=[],
            minibarConsumed=True,
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
            services=[BREAKFAST],
            minibarConsumed=True,
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
            services=[BREAKFAST],
            minibarConsumed=False,
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
            services=[BREAKFAST],
            minibarConsumed=False,
        )
    )
    assert invoice == expected_invoice


def test_calculate_standard_invoice_when_platinum_subscription_and_state_BA():
    expected_invoice = {
        'roomPrice': 36000,
        'minibar': 0,
        'breakfast': 0,
        'total': 19998,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=4,
            state='BA',
            subscription=PLATINUM_SUB,
            room=STANDARD_ROOM,
            services=[BREAKFAST],
            minibarConsumed=False,
        )
    )
    assert invoice == expected_invoice


def test_calculate_standard_invoice_when_platinum_subscription_and_state_PE():
    expected_invoice = {
        'roomPrice': 36000,
        'minibar': 0,
        'breakfast': 0,
        'total': 20097,
    }
    invoice = calculateInvoice(
        StayInformations(
            nights=4,
            state='PE',
            subscription=PLATINUM_SUB,
            room=STANDARD_ROOM,
            services=[BREAKFAST],
            minibarConsumed=False,
        )
    )
    assert invoice == expected_invoice

