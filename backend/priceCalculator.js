var WebmasterAPI = require('webmaster-api');
WebmasterAPI.init("your API key");


/*TODO: Create costBasis method, 
        Percentage Inc/Dec method,
        Decide what goes under PriceCalculator vs DirectPriceCalculator
*/
class PriceCalculator {
    constructor() {

    }

    canPurchase(searchTerm, amount) {
        //Check if User can purchase a searchTerm 
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
  
    currentPrice(searchTerm) {
        //Price of a search term is the volume over the last 24 hours
        var yesterday = new Date(Date.now() - 86400 * 1000).toISOString();
        var today = Date.now().toISOString();
        return volume = webMasterAPI(searchTerm, yesterday, today); 
    }

}


exports.PriceCalculator = PriceCalculator
exports.DirectPriceCalculator = DirectPriceCalculator
