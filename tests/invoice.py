import pytest
from app.hotel import calculate_invoice


def test_calculate_presidential_invoice():
    expected_invoice = {
        'roomPrice': 34000,
        'minibar': 0,
        'breakfast': 0,
        'total': 24276,
    }
    invoice = calculate_invoice(
        nights=2,
        state='SP',
        room_name='presidential',
        is_subscriber=True,
        minibar_consumed=True,
        breakfast_added=False
    )
    assert invoice == expected_invoice


def test_calculate_deluxe_invoice():
    expected_invoice = {
        'roomPrice': 42000,
        'minibar': 7500,
        'breakfast': 2500,
        'total': 53040,
    }
    invoice = calculate_invoice(
        nights=3,
        state='SP',
        room_name='deluxe',
        is_subscriber=False,
        minibar_consumed=True,
        breakfast_added=True
    )
    assert invoice == expected_invoice


def test_calculate_standard_invoice():
    expected_invoice = {
        'roomPrice': 36000,
        'minibar': 0,
        'breakfast': 2500,
        'total': 39655,
    }
    invoice = calculate_invoice(
        nights=4,
        state='RJ',
        room_name='standard',
        is_subscriber=False,
        minibar_consumed=False,
        breakfast_added=True
    )
    assert invoice == expected_invoice
