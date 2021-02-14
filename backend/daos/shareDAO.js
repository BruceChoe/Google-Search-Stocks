// class SQLShareDAO {
//   constructor(db, priceCalculator) {
//     this.db = db;
//     this.priceCalculator = priceCalculator;
//
//     const that = this;
//
//     this.db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='Shares';",
//       [],
//       function (err, row) {
//         if (row === undefined) {
//           that.db.run('CREATE TABLE Shares (ID INTEGER PRIMARY KEY, Term TEXT, Test Integer);');
//         }
//       });
//   }
//
//   create(share) {
//     let id = undefined;
//
//     this.db('' +
//       'INSERT INTO Shares (Term)' +
//       'VALUES (\'?\');',
//       share.term,
//       function () {
//         id = this.lastID;
//       })
//
//     return id;
//   }
// }
//
// exports.SQLShareDAO = SQLShareDAO;