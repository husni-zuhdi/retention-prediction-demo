require("dotenv").config()
const express = require('express');
const bodyParser = require('body-parser');

// Setup server port
const port = process.env.PORT || 8080;

// create express app
const app = express();

// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }))
// parse requests of content-type - application/json
app.use(bodyParser.json())

// define a root route
const auth = require('./src/controllers/auth')
const predict = require('./src/controllers/predict')
app.post('/predict', predict.predict);

// listen for requests
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});