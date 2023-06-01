from app.models.stay_informations import StayInformations


def calculateInvoice(stay_information: StayInformations):
    return {
        'roomPrice': stay_information.calculate_room_price(),
        'minibar': stay_information.calculate_minibar_fee(),
        **stay_information.additional_services_fee(),
        'total': apply_taxation(stay_information.calculate_total_amount(), stay_information.state),
    }


state_fee_mapper = {
    'SP': 0.02,
    'RJ': 0.03,
    'BA': 0.01,
    'PE': 0.015,
}


def apply_taxation(amount, state):
    return amount + amount * state_fee_mapper[state]
