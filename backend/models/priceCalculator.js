// const WebmasterAPI = require('webmaster-api');
// WebmasterAPI.init("your API key");

/**
 * The interface for PriceCalculator classes. This class can also be used as a mock for testing.
 */
class PriceCalculator {
    /**
     * Instantiate a PriceCalculator object.
     */
    constructor() {}

    /**
     * Calculate the current price for the given search term.
     *
     * @param {string} searchTerm The search term in question.
     */
    currentPrice(searchTerm) {
        return 50.
    }
}

/**
 * A PriceCalculator that determines the price of a search term based solely on that
 * search term's popularity, and not other search terms that are similar.
 */
class DirectPriceCalculator {
    /**
     * Instantiate a DirectPriceCalculator.
     *
     * @param webMasterAPI A WebMasterAPI object used to determine the interest in a search term.
     */
    constructor(webMasterAPI) {
        this.webMasterAPI = webMasterAPI
    }

    /**
     * Find the current price of the given search term.
     *
     * @param searchTerm The search term in question.
     * @returns {number} The current market price of the search term.
     */
    currentPrice(searchTerm) {
        // WebMasterAPI needs both today's date and yesterday's date.
        const yesterday = new Date(Date.now() - 86400 * 1000).toISOString();
        const today = new Date(Date.now()).toISOString();

        // TODO: Scaling to make values better for user?

        return this.webMasterAPI(searchTerm, yesterday, today);
    }

}


exports.PriceCalculator = PriceCalculator
exports.DirectPriceCalculator = DirectPriceCalculator
