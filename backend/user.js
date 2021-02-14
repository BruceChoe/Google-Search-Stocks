/*
 * Users Class File
*/

class User {
    constructor(inventory, transactionHistory, market) { //dependency injection
        this.inventory = inventory;
        this.transactionHistory = transactionHistory;
        this.market = market;
    }

    buy(searchTerm, amount) {
        this.market(searchTerm, amount, this.inventory);
    }

    sell(searchTerm, amount) {
        this.market(searchTerm, amount, this.inventory);
    }


}