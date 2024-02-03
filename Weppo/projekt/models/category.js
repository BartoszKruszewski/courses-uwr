const db = require("../database");

const createTable = () => {
  db.run(
    `CREATE TABLE IF NOT EXISTS 
    categories
    (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL
    )`
  );
};

const get = () => {
  return new Promise((resolve, reject) => {
    db.all("SELECT id, name FROM categories", (err, categories) => {
      if (err) reject(err);
      else resolve(categories);
    });
  });
};

const add = (name) => {
  return new Promise((resolve, reject) => {
    db.run("INSERT INTO categories (name) VALUES (?)", [name], (err) => {
      if (err) reject(err);
      else resolve();
    });
  });
};

module.exports = { createTable, get, add };
