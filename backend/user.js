/*
 * Users Class File
*/

class user {
    constructor(inventory, transactionHistory, market) { //dependency injection
        this.inventory = inventory;
        this.transactionHistory = transactionHistory;
        this.market = market;
    }

    buy(searchTerm, amount) {
        //TODO
    }

    sell(searchTerm, amount) {
        //TODO
    }
}