const assert = require("assert");
const {DirectPriceCalculator} = require("../../models/priceCalculator");

class MockWebMasterAPI {
  constructor() {
    return function (searchTerm, yesterday, today) {
      return 50.;
    }
  }
}

describe('DirectPriceCalculator', function () {
  describe('#currentPrice(searchTerm)', function () {
    it("should return the volume based on WebMasterAPI", function (done) {
      const webMasterApi = new MockWebMasterAPI();
      const priceCalculator = new DirectPriceCalculator(webMasterApi);

      // TODO: Figure out a better way to mock out dates.
      assert.strictEqual(priceCalculator.currentPrice("avocados"),
        webMasterApi("avocados", undefined, undefined));

      done();
    })
  })
})