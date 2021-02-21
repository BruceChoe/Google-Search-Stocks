/*
 * Inventory Class File
*/

class inventory {
    constructor() {
        this.money = 100000000;
    }

    addShare(searchTerm, amount) {
        if (stocks[searchTerm] === undefined) {
            stocks[searchTerm] = amount; 
        } else {
            stocks[searchTerm] = stocks[searchTerm] + amount; 
        }
    }

    removeShare(searchTerm, amount) {
        if (stocks[searchTerm] === undefined) {
            // If share does not exist, throw error code
        } else if (amount > stocks[searchTerm]) {
             //TODO: If amount exceeds current amount of shares, throw error. 
        } else {
            stocks[searchTerm] = stocks[searchTerm] - amount;
        }
    }
}

