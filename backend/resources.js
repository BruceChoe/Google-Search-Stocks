const sqlite3 = require('sqlite3').verbose();

const DB = new sqlite3.Database('db.sqlite3')

exports.DB = DB;