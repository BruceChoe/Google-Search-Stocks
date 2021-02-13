class PriceCalculator {
    constructor(searchTerm) {
        this.currentDate = new Date();
        this.searchTerm = searchTerm;
        this.volume = webMasterAPI(searchTerm, currentDate - 1, currentDate); //get volume data from yesterday to today
    }
}

class DirectPriceCalculator {
    constructor(searchTerm) {
        this.currentDate = new Date();
        this.searchTerm = searchTerm;
        this.volume = webMasterAPI(searchTerm, currentDate - 1, currentDate); //get volume data from yesterday to today, TODO: API PLACEHOLDER
    }
  
    calculatePrice(searchTerm) {
        return volume; 
    }

    // Accessors, Getters
    get currentDate() {
        return currentDate;
    }

    get searchTerm() {
        return searchTerm;
    }

    get volume() {
        return webMasterAPI(searchTerm, currentDate - 1, currentDate);
    }

    // Mutators, Setters
    set currentDate(date) {
        this.currentDate = date;
    }

    
}

exports.PriceCalculator = PriceCalculator
exports.DirectPriceCalculator = DirectPriceCalculator
