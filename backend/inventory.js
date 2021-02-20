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
        } else {
            stocks[searchTerm] = stocks[searchTerm] - amount; //TODO: If amount exceeds current amount of shares, 
        }
    }
}

stocks = new Object();
stocks["h"] = 1;
console.log(stocks["h"]);
stocks["h"] = stocks["h"] + 1;
console.log(stocks["h"]);