/*
 * Inventory Class File
*/

class inventory {
    constructor() {
        this.balance = 100000000;
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
            // TODO: If share does not exist, throw error code
        } else if (amount > stocks[searchTerm]) {
             //TODO: If amount exceeds current amount of shares, throw error. 
        } else {
            stocks[searchTerm] = stocks[searchTerm] - amount;
        }
    }
}

let myInventory = new inventory();
console.log(myInventory.money);
