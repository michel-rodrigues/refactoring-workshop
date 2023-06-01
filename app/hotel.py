from app.models.stay_informations import StayInformations


def calculateInvoice(stay_information: StayInformations):
    return {
        'roomPrice': stay_information.calculate_room_price(),
        'minibar': stay_information.calculate_minibar_fee(),
        **stay_information.additional_services_fee(),
        'total': apply_taxation(stay_information.calculate_total_amount(), stay_information.state),
    }


def apply_taxation(amount, state):
    if state == 'SP':
        return amount + amount * 0.02
    return amount + amount * 0.03
