const extraFees = require('./constants/extraFees')
const plans = require('./constants/plans')
const rooms = require('./rooms.json')


function calculateInvoice({ nights, roomName, state, plan, minibarConsumed, breakfastAdded }) {

  const room = rooms[roomName]
  plan = plan || plans.free

  return {
    roomPrice: calculateRoomPrice({ nights, room }),
    minibar: calculateMinibarFee({ room, minibarConsumed }, plan),
    breakfast: calculateBreakfastFee({ breakfastAdded }, plan),
    total: calculateTotal({ nights, minibarConsumed, breakfastAdded, room }, plan, state),
  }
}

function calculateFees({ minibarConsumed, breakfastAdded, room }, plan) {

  return calculateBreakfastFee({ breakfastAdded }, plan) + calculateMinibarFee({ room, minibarConsumed }, plan)
}

function calculateMinibarFee({ room, minibarConsumed }, plan) {
  let minibarFee = minibarConsumed && room.minibarFee ? room.minibarFee : 0

  if (!plan.cashInMinibar) {
    minibarFee = 0
  }

  return minibarFee
}

function calculateBreakfastFee({ breakfastAdded }, plan) {
  let breakfastPrice = 2500

  if (!plan.cashInBreakfast || !breakfastAdded) {
    breakfastPrice = 0
  }
  return breakfastPrice
}

function calculateTotal({ minibarConsumed, breakfastAdded, room, nights }, plan, state) {
  let total = calculateRoomPrice({ room, nights }) + calculateFees({ minibarConsumed, breakfastAdded, room }, plan)


  total = total - (total * plan.totalDiscount)


  const localizationFees = extraFees[state.toUpperCase()] || extraFees.default

  total = total + (total * localizationFees)
  return total
}

function calculateRoomPrice({ room, nights }) {
  return room.price * nights
}

module.exports = calculateInvoice
