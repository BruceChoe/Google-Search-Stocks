class UserDAO {
  constructor(db) {
    this.db = db;

    const that = this;

    this.db.get("SELECT name FROM sqlite_master WHERE type='table' AND name='Users';",
      [],
      function (err, row) {
        if (row === undefined) {
          that.db.run('CREATE TABLE Users (ID INTEGER PRIMARY KEY);');
        }
      });
  }

  create() {
    let id = undefined;

    this.db('' +
      'INSERT INTO Users (Name)' +
      'VALUES (\'Jerry\');',
      function () {
        id = this.id;
      });

    return id;
  }

  read(id) {
    let user = undefined;

    this.db.get(`SELECT Name FROM Users WHERE id=${id};`,
      function (err, row) {
        user = row;
      });

    return user;
  }
}

module.exports = UserDAO;