const fs = require("fs");
const path = require("path");
const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database("database.db");

module.exports = db;
let models = {};

fs.readdirSync(__dirname + "/../models").forEach((file) => {
  if (file.endsWith(".js")) {
    model_name = file.replace(".js", "");
    models[model_name] = require(path.join(__dirname + "/../models", file));
    models[model_name].createTable();
  }
});

module.exports = { db, models };
