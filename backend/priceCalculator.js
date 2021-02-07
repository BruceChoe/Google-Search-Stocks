class PriceCalculator {
  constructor(props) {}

  calculate(term) {
    return 50.
  }
}

// TODO @Bruce: Create a "DirectPriceCalculator" that calculates the price of a term based on only that term's
// popularity, not on other terms related to it.
//test push

const x = 1;
myDate = new Date();
console.log(myDate);
myDate.setDate(myDate.getDate() - 1);
console.log(myDate);

class DirectPriceCalculator {
    constructor(searchTerm) {
        this.currentDate = new Date();
        this.searchTerm = searchTerm;
        this.volume = webMasterAPI(searchTerm, currentDate - 1, currentDate);
    }
  
    calculate(term) {
      return 50.
    }

    get volume() {
        //return webMasterAPI(this.searchTerm,
    }
}

exports.PriceCalculator = PriceCalculator
exports.DirectPriceCalculator = DirectPriceCalculator
