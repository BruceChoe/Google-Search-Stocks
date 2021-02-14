/*
 * Market Class File
*/

class Market {
    constructor(priceCalculator) {
        this.priceCalculator = priceCalculator;
    }

    buy(searchTerm, amount, inventory) {
        if (searchTerm.priceCalculator.currentPrice * amount < 10/*TODO: Compare with users amount of money*/) {
            // execute order
        } else {
            // Don't execute order
        }
    }

    sell(searchTerm, amount, inventory) {
        if (this.inventory.)
    }
}