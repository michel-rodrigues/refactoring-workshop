def calculateInvoice(nights, room, state, isSubscriber, minibarConsumed, breakfastAdded):
    # Calculate the total amount of the invoice
    total = calculate_total_amount(nights, room, minibarConsumed, breakfastAdded)
    minibarFee, total = apply_discount(isSubscriber, calculate_minibar_fee(minibarConsumed, room), total)
    total = apply_taxation(state, total)

    return {
        'roomPrice': calculate_room_price(nights, room),
        'minibar': minibarFee,
        'breakfast': calculate_breakfast_fee(breakfastAdded),
        'total': total,
    }

def apply_discount(isSubscriber, minibarFee, total):
    if isSubscriber:
        total = total - minibarFee
        minibarFee = 0
        total = total - total * 0.3
    return minibarFee, total

def calculate_total_amount(nights, room, minibarConsumed, breakfastAdded):
    return calculate_room_price(nights, room) + calculate_minibar_fee(minibarConsumed, room) + calculate_breakfast_fee(breakfastAdded)

def calculate_breakfast_fee(breakfastAdded):
    return 2500 if breakfastAdded else 0

def calculate_minibar_fee(minibarConsumed, room):
    return room.minibarFee if minibarConsumed else 0

def calculate_room_price(nights, room):
    return room.price * nights

def apply_taxation(state, total):
    if state == 'SP':
        return total + total * 0.02
    return total + total * 0.03