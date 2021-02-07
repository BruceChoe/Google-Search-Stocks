class PriceCalculator {
  constructor(props) {}

  calculate(term) {
    return 50.
  }
}

// TODO @Bruce: Create a "DirectPriceCalculator" that calculates the price of a term based on only that term's
// popularity, not on other terms related to it.

class DirectPriceCalculator {
  constructor(props) {}

  calculate(term) {
    return 50.
  }
}

exports.PriceCalculator = PriceCalculator
exports.DirectPriceCalculator = DirectPriceCalculator
