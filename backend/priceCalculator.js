var WebmasterAPI = require('webmaster-api');
WebmasterAPI.init("your API key");


/*TODO: Create costBasis method, 
        Percentage Inc/Dec method,
        Decide what goes under PriceCalculator vs DirectPriceCalculator
*/
class PriceCalculator {
    constructor() {

    }

    /*
     * canPurchase(searchTerm, amount) method
     * Desc: Checks if a buy order is exectuable
     * Input: Search Term, amount of shares to buy
     * Output: Boolean True/False 
    */
    canPurchase(searchTerm, amount) {
        if (this.calculateCurrentPrice(searchTerm) * amount < (10/*TODO: USER MONEY VARIABLE*/)) {
            return true;
        } else {
            return false;
        }
    }
    
}



class DirectPriceCalculator {
    constructor() {

    }

    /*
     * currentPrice(searchTerm) method
     * Input: searchTerm
     * Output: Price of a single share of searchTerm 
     * Calculates price by taking volume over the last 24 hours
    */
    currentPrice(searchTerm) {
        var yesterday = new Date(Date.now() - 86400 * 1000).toISOString();
        var today = Date.now().toISOString();
        return volume = webMasterAPI(searchTerm, yesterday, today); 
    }

}


exports.PriceCalculator = PriceCalculator
exports.DirectPriceCalculator = DirectPriceCalculator
