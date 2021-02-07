const express = require('express');
const {DirectPriceCalculator} = require("../priceCalculator");
const router = express.Router();

const priceCalculator = new DirectPriceCalculator();

/**
 * @param req.query.term The term to find the price for.
 */
router.get('/', function (req, res) {
  // Query parameters
  const term = req.query.term;

  res.json({'price': priceCalculator.calculate(term)})
});

module.exports = router;