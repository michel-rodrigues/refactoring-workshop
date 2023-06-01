const calculateInvoice = require('../app/hotel');
const plans = require('../app/constants/plans')

test('calculate presidential invoice for plan gold in SP', () => {
  expectedInvoice = {
    roomPrice: 34000,
    minibar: 0,
    breakfast: 0,
    total: 24276,
  }
  const invoice = calculateInvoice({
    nights: 2,
    state: 'SP',
    roomName: 'presidential',
    plan: plans.gold,
    minibarConsumed: true,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});

test('calculate deluxe invoice for plan free in SP', () => {
  expectedInvoice = {
    roomPrice: 42000,
    minibar: 7500,
    breakfast: 2500,
    total: 53040,
  }
  const invoice = calculateInvoice({
    nights: 3,
    state: 'SP',
    roomName: 'deluxe',
    plan: plans.free,
    minibarConsumed: true,
    breakfastAdded: true,
  })
  expect(invoice).toEqual(expectedInvoice)
});

test('calculate standard invoice for plan free in RJ', () => {
  expectedInvoice = {
    roomPrice: 36000,
    minibar: 0,
    breakfast: 2500,
    total: 39655,
  }
  const invoice = calculateInvoice({
    nights: 4,
    state: 'RJ',
    roomName: 'standard',
    plan: plans.free,
    minibarConsumed: false,
    breakfastAdded: true,
  })
  expect(invoice).toEqual(expectedInvoice)
});

test('calculate standard invoice for plan platinum in RJ', () => {
  expectedInvoice = {
    roomPrice: 36000,
    minibar: 0,
    breakfast: 0,
    total: 20394,
  }
  const invoice = calculateInvoice({
    nights: 4,
    state: 'RJ',
    roomName: 'standard',
    plan: plans.platinum,
    minibarConsumed: false,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});


test('calculate standard invoice for plan platinum in SP', () => {
  expectedInvoice = {
    roomPrice: 36000,
    minibar: 0,
    breakfast: 0,
    total: 20196,
  }
  const invoice = calculateInvoice({
    nights: 4,
    state: 'SP',
    roomName: 'standard',
    plan: plans.platinum,
    minibarConsumed: false,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});


test('calculate deluxe invoice for plan platinum in SP', () => {
  expectedInvoice = {
    roomPrice: 56000,
    minibar: 0,
    breakfast: 0,
    total: 31416,
  }
  const invoice = calculateInvoice({
    nights: 4,
    state: 'SP',
    roomName: 'deluxe',
    plan: plans.platinum,
    minibarConsumed: false,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});

test('calculate deluxe invoice for plan platinum in RJ', () => {
  expectedInvoice = {
    roomPrice: 56000,
    minibar: 0,
    breakfast: 0,
    total: 31724,
  }
  const invoice = calculateInvoice({
    nights: 4,
    state: 'RJ',
    roomName: 'deluxe',
    plan: plans.platinum,
    minibarConsumed: false,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});


test('calculate presidential invoice for plan platinum in RJ', () => {
  expectedInvoice = {
    roomPrice: 68000,
    minibar: 0,
    breakfast: 0,
    total: 38522,
  }
  const invoice = calculateInvoice({
    nights: 4,
    state: 'RJ',
    roomName: 'presidential',
    plan: plans.platinum,
    minibarConsumed: false,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});

test('calculate presidential invoice for plan platinum in SP', () => {
  expectedInvoice = {
    roomPrice: 68000,
    minibar: 0,
    breakfast: 0,
    total: 38148,
  }
  const invoice = calculateInvoice({
    nights: 4,
    state: 'SP',
    roomName: 'presidential',
    plan: plans.platinum,
    minibarConsumed: false,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});


