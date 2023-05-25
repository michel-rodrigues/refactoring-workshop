const { getMinibarFee } = require('../app/hotel');

test("minibarfee", () => {
    const params = [
        { minibarFee: 7500, minibarConsumed: true, isMinibarFree: false, expectedFee: 7500 },
        { minibarFee: 7500, minibarConsumed: false, isMinibarFree: false, expectedFee: 0 },
        { minibarFee: 7500, minibarConsumed: true, isMinibarFree: true, expectedFee: 0 },
        { minibarFee: 7500, minibarConsumed: false, isMinibarFree: true, expectedFee: 0 },
        { minibarFee: 0, minibarConsumed: true, isMinibarFree: false, expectedFee: 0 },
    ]
    params.forEach(param => {
        const { minibarFee, minibarConsumed, isMinibarFree, expectedFee } = param
        const minibar = getMinibarFee(minibarFee, minibarConsumed, isMinibarFree)
        expect(minibar).toBe(expectedFee)
    })
})
