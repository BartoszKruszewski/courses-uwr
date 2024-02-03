const db = require("../database");

const createTable = () => {
  db.run(
    `CREATE TABLE IF NOT EXISTS 
    users
    (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT UNIQUE NOT NULL,
      hmac TEXT NOT NULL
    )`
  );
};

const getAll = () => {
  return new Promise((resolve, reject) => {
    db.all("SELECT email FROM users", (err, users) => {
      if (err) reject(err);
      else resolve(users);
    });
  });
};

const get = (email) => {
  return new Promise((resolve, reject) => {
    db.get(
      "SELECT email, hmac FROM users WHERE email = ?",
      [email],
      (err, user) => {
        if (err) reject(err);
        else resolve(user);
      }
    );
  });
};

const add = (email, hmac) => {
  return new Promise((resolve, reject) => {
    db.run(
      "INSERT INTO users (email, hmac) VALUES (?, ?)",
      [email, hmac],
      (err) => {
        if (err) reject(err);
        else resolve();
      }
    );
  });
};

module.exports = { createTable, get, add, getAll };
