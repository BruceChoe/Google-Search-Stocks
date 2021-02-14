// const assert = require('assert');
// const {SQLShareDAO} = require("../../daos/shareDAO");
// const {PriceCalculator} = require("../../priceCalculator");
// const sqlite3 = require('sqlite3').verbose()
//
// describe('ShareDAO', function () {
//   const db = new sqlite3.Database('mytest.sqlite3');
//
//   after(function () {
//     // db.run("DROP TABLE Shares");
//     // db.close();
//   })
//
//   describe('#constructor(db, shareCalculator)', function () {
//     it("should create a new 'Shares' table", function (done) {
//       new SQLShareDAO(db, new PriceCalculator());
//
//       db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='Shares';", [],
//         function (err, row) {
//           assert.notStrictEqual(row, undefined);
//         })
//
//       done();
//     })
//   })
// })