from app.models.stay_informations import StayInformations


def calculateInvoice(stay_information: StayInformations):
    # Calculate the total amount of the invoice
    total = stay_information.calculate_total_amount()
    total = apply_taxation(stay_information.state, total)

    return {
        'roomPrice': stay_information.calculate_room_price(),
        'minibar': stay_information.calculate_minibar_fee(),
        'breakfast': stay_information.calculate_breakfast_fee(),
        'total': total,
    }


def apply_taxation(state, total):
    if state == 'SP':
        return total + total * 0.02
    return total + total * 0.03
