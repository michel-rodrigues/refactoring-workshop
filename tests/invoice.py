import pytest

from app.Invoice import Invoice
from app.hotel import calculate_invoice
from app.rooms import PresidentialRoom, StandardRoom, DeluxeRoom
from app.subscriber import GoldSubscriber, NonSubscriber, PlatinumSubscriber


def test_calculate_presidential_invoice():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'breakfast': 0,
        'total': 24276,
    }
    new_invoice = Invoice(
        nights=2,
        room=PresidentialRoom(),
        subscriber=GoldSubscriber(),
        services={'minibar': False, 'breakfast': False})
    invoice = calculate_invoice(new_invoice, state='SP')

    assert invoice == expected_invoice


def test_calculate_deluxe_invoice():
    expected_invoice = {
        'roomPrice': 42000,
        'minibar': 7500,
        'breakfast': 2500,
        'total': 53040,
    }

    new_invoice = Invoice(nights=3, room=DeluxeRoom(), subscriber=NonSubscriber(), services={
        'minibar': True,
        'breakfast': True
    })

    invoice = calculate_invoice(new_invoice, state='SP')
    assert invoice == expected_invoice


def test_calculate_standard_invoice():
    expected_invoice = {
        'roomPrice': 36000,
        'minibar': 0,
        'breakfast': 2500,
        'total': 39655,
    }

    new_invoice = Invoice(nights=4, room=StandardRoom(), subscriber=NonSubscriber(), services={
        'minibar': False,
        'breakfast': True
    })

    invoice = calculate_invoice(new_invoice, state='RJ')
    assert invoice == expected_invoice


def test_calculate_platinum_invoice():
    expected_invoice = {
        'roomPrice': 51000,
        'minibar': 0,
        'breakfast': 0,
        'total': 28891.5,
    }

    new_invoice = Invoice(nights=3, room=PresidentialRoom(), subscriber=PlatinumSubscriber(), services={
        'minibar': False,
        'breakfast': False
    })

    invoice = calculate_invoice(
        new_invoice,
        state='RJ',
    )
    assert invoice == expected_invoice
