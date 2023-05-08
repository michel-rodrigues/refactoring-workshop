const rooms = require('./rooms.json')


function calculateInvoice({ nights, roomName, state, isSubscriber, minibarConsumed, breakfastAdded }) {
  const room = rooms[roomName]

  const roomPrice  = room.price * nights

  var minibarFee = minibarConsumed && room.minibarFee ? room.minibarFee : 0
  if (isSubscriber) {
    minibarFee = 0
  }

  const breakfastFee = breakfastAdded ? 2500 : 0

  // Calculate the total amount of the invoice
  var total = roomPrice + minibarFee + breakfastFee
  if (isSubscriber) {
    total = total - (total * 0.3)
  }
  if (state === 'SP') {
    total = total + (total * 0.02)
  } else {
    total = total + (total * 0.03)
  }

  return {
    roomPrice: roomPrice,
    minibar: minibarFee,
    breakfast: breakfastFee,
    total: total,
  }
}

module.exports = calculateInvoice
