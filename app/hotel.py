from app.Invoice import Invoice

STATES_TAX = {"SP": 0.02, "RJ": 0.03}


def calculate_minibar(invoice: Invoice):
    return invoice.room.minibarFee if invoice.services["minibar"] and not invoice.subscriber.minibarCourtesy else 0


def calculate_breakfast(invoice: Invoice):
    return invoice.subscriber.breakfastTax if invoice.services['breakfast'] else 0


def calculate_sauna(invoice: Invoice):
    return 3000 if invoice.services['sauna'] else 0


def calculate_massage(invoice: Invoice):
    return 7500 if invoice.services['massage'] else 0


SERVICES = {
    "minibar": calculate_minibar,
    "breakfast": calculate_breakfast,
    "sauna": calculate_sauna,
    "massage": calculate_massage
}


def calculate_invoice(invoice: Invoice, state: str) -> dict:
    room_price = {"roomPrice": invoice.room.calculate_room_price(invoice.nights)}
    services = {service_name: SERVICES[service_name](invoice) for (service_name, service_status) in
                invoice.services.items()}

    total = {"total": get_total(room_price, services, state, invoice.subscriber)}

    return room_price | services | total


def get_total(room_price, services, state, subscriber):
    total = room_price["roomPrice"]
    total_services = sum(services.values())
    total = total + total_services
    total -= total * subscriber.totalDiscount

    total_with_tax = get_state_tax(state, total)

    return total_with_tax


def get_state_tax(state: str, total: float) -> float:
    total += total * STATES_TAX[state]
    return total
