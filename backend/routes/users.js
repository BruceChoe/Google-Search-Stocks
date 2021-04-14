const express = require('express');
const UserDAO = require("../daos/userDAO");
const {DB} = require("../resources");
const router = express.Router();


// /* GET users listing. */
// router.get('/', function(req, res, next) {
//   res.send('respond with a resource');
// });

router.post('/', function (req, res, next) {
  const dao = new UserDAO(DB);

  const id = dao.create();

  res.json({id: id});
})

module.exports = router;
