from app.rooms import ROOMS


def calculate_invoice(nights, room_name, state, is_subscriber, minibar_consumed, breakfast_added):
    room = ROOMS[room_name]

    room_price = room['price'] * nights

    minibar_fee = room['minibarFee'] if minibar_consumed and room.get('minibarFee') else 0
    if is_subscriber:
        minibar_fee = 0

    breakfast_fee = 2500 if breakfast_added else 0

    total = room_price + minibar_fee + breakfast_fee
    if is_subscriber:
        total -= total * 0.3

    if state == 'SP':
        total += total * 0.02
    else:
        total += total * 0.03

    return {
        'roomPrice': room_price,
        'minibar': minibar_fee,
        'breakfast': breakfast_fee,
        'total': total
    }
