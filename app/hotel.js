const extraFees = require('./constants/extraFees')
const rooms = require('./rooms.json')


function calculateInvoice({ nights, roomName, state, isSubscriber, minibarConsumed, breakfastAdded }) {
  const room = rooms[roomName]

  const roomPrice = room.price * nights

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

  const fees = extraFees[state.toUpperCase()] || extraFees.default

  total = total + (total * fees)

  return {
    roomPrice: roomPrice,
    minibar: minibarFee,
    breakfast: breakfastFee,
    total: total,
  }
}

module.exports = calculateInvoice
