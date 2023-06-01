const extraFees = require('./constants/extraFees')
const plans = require('./constants/plans')
const servicesFees = require('./constants/servicesFees')
const rooms = require('./rooms.json')


function calculateInvoice({ nights, roomName, state, plan, services }) {

  const room = rooms[roomName]
  plan = plan || plans.free

  return {
    roomPrice: calculateRoomPrice({ nights, room }),
    minibar: calculateMinibarFee({ room, minibarConsumed: services.minibarConsumed }, plan),
    breakfast: calculateBreakfastFee({ breakfastAdded: services.breakfastAdded }, plan),
    total: calculateTotal({ nights, services, room }, plan, state),
  }
}

function calculateFees({ services, room }, plan) {

  return calculateBreakfastFee({ breakfastAdded: services.breakfastAdded }, plan) +
    calculateMinibarFee({ room, minibarConsumed: services.minibarConsumed }, plan) +
    calculateSaunaFee(services.saunaAdded) +
    calculateMassageFee(services.massageAdded)
}

function calculateSaunaFee(saunaAdded) {
  return saunaAdded ? servicesFees.sauna.total : 0
}

function calculateMassageFee(massageAdded) {
  return massageAdded ? servicesFees.massage.total : 0
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

function calculateTotal({ services, room, nights }, plan, state) {

  let total = calculateRoomPrice({ room, nights }) + calculateFees({ services, room }, plan)


  console.log(total)
  total = total - (total * plan.totalDiscount)


  const localizationFees = extraFees[state.toUpperCase()] || extraFees.default

  total = total + (total * localizationFees)
  return total
}

function calculateRoomPrice({ room, nights }) {
  return room.price * nights
}

module.exports = calculateInvoice
