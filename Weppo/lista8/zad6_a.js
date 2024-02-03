var crypto = require("crypto");

var http = require("http");
var express = require("express");
var app = express();

app.set("view engine", "ejs");
app.set("views", "./views");
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.end("default page");
});

app.get("/faktura/:id", (req, res) => {
  var secret = "this is a secret";
  var parameter = req.params.id;
  var correct_mac = crypto
    .createHmac("sha256", secret)
    .update(parameter)
    .digest("hex");

  // id 1448219
  // mac d4d07c762f416897d9d4016f51b2ff3b634ec1020ce33c6d86fdd151f7a12e3e
  // http://localhost:3000/faktura/1448219?mac=d4d07c762f416897d9d4016f51b2ff3b634ec1020ce33c6d86fdd151f7a12e3e

  var query_mac = req.query.mac;
  if (query_mac == correct_mac)
    res.end(`dynamicznie generowana faktura:${req.params.id}`);
  else res.end("Bledy mac!");
});

http.createServer(app).listen(3000);
