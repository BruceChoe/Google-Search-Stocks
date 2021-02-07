class Share {
  constructor(term, priceCalculator) {
    this.term = term;
    this.priceCalculator = priceCalculator;
  }

  get price() {
    return this.priceCalculator.calculate(this.term);
  }
}