const rooms = require('./rooms.json')
const subscriptions = require('./subscriptions.json')
const taxes = require('./taxes.js')

function calculateInvoice(bookingData) {
  const { nights, roomName, state, subscriptionPlan, minibarConsumed, breakfastAdded } = bookingData
  const room = rooms[roomName]
  const subscription = subscriptions[subscriptionPlan]

  var total = getRoomPrice(bookingData) + getMinibarFee(bookingData) + getBreakfastFee(subscription.isBreakfastFree, breakfastAdded)
  total = total * (1 - subscription.discount)
  total = total * (1 + taxes[state])

  return {
    roomPrice: getRoomPrice(bookingData),
    minibar: getMinibarFee(room.minibarFee, minibarConsumed, subscription.isMinibarFree),
    breakfast: getBreakfastFee(subscription.isBreakfastFree, breakfastAdded),
    total: total,
  }
}

const getRoomPrice = ({ roomName, nights }) => {
  return rooms[roomName].price * nights
}

const getBreakfastFee = (isBreakfastFree, breakfastAdded) => {
  if (breakfastAdded && !isBreakfastFree) {
    return 2500
  }
  return 0
}

const getMinibarFee = ({ roomName, minibarConsumed, subcriptionPlan}) => {
  if (minibarConsumed && rooms[roomName].minibarFee && !subscriptions[subcriptionPlan].isMinibarFree) {
    return rooms[roomName].minibarFee
  }
  return 0
}

module.exports = { calculateInvoice, getMinibarFee }
