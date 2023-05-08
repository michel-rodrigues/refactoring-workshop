const calculateInvoice = require('../app/hotel');

test('calculate presidential invoice', () => {
  expectedInvoice = {
    roomPrice: 34000,
    minibar: 0,
    breakfast: 0,
    total: 23800,
  }
  const invoice = calculateInvoice({
    nights: 2,
    roomName: 'presidential',
    isSubscriber: true,
    minibarConsumed: true,
    breakfastAdded: false,
  })
  expect(invoice).toEqual(expectedInvoice)
});

test('calculate deluxe invoice', () => {
  expectedInvoice = {
    roomPrice: 42000,
    minibar: 7500,
    breakfast: 2500,
    total: 52000,
  }
  const invoice = calculateInvoice({
    nights: 3,
    roomName: 'deluxe',
    isSubscriber: false,
    minibarConsumed: true,
    breakfastAdded: true,
  })
  expect(invoice).toEqual(expectedInvoice)
});

test('calculate standard invoice', () => {
  expectedInvoice = {
    roomPrice: 36000,
    minibar: 0,
    breakfast: 2500,
    total: 38500,
  }
  const invoice = calculateInvoice({
    nights: 4,
    roomName: 'standard',
    isSubscriber: false,
    minibarConsumed: false,
    breakfastAdded: true,
  })
  expect(invoice).toEqual(expectedInvoice)
});
