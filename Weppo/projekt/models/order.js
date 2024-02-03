const db = require("../database");

function actualDateString() {
  const date = new Date();
  const year = date.getFullYear();
  const month = ("0" + (date.getMonth() + 1)).slice(-2);
  const day = ("0" + date.getDate()).slice(-2);
  const hours = ("0" + date.getHours()).slice(-2);
  const minutes = ("0" + date.getMinutes()).slice(-2);
  const seconds = ("0" + date.getSeconds()).slice(-2);

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

const createTable = () => {
  db.run(
    `CREATE TABLE IF NOT EXISTS 
    orders
    (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      datetime TEXT NOT NULL,
      status TEXT NOT NULL,
      user_id INTEGER NOT NULL,
      FOREIGN KEY (user_id) REFERENCES users(id)
    )`
  );
};

const getAll = () => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT 
      orders.id AS id, 
      orders.datetime AS datetime, 
      orders.status AS status,
      users.email AS user 
    FROM orders
    JOIN users ON orders.user_id = users.id`,
      (err, orders) => {
        if (err) reject(err);
        else resolve(orders);
      }
    );
  });
};

const get = (user) => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT id, datetime, status
      FROM orders
      WHERE user_id = (SELECT id FROM users WHERE email = ?)`,
      [user],
      (err, orders) => {
        if (err) reject(err);
        else resolve(orders);
      }
    );
  });
};

const getLastID = () => {
  return new Promise((resolve, reject) => {
    db.get("SELECT id FROM orders ORDER BY id DESC LIMIT 1;", (err, order) => {
      if (err) reject(err);
      else resolve(order.id);
    });
  });
};

const add = (user_email) => {
  return new Promise((resolve, reject) => {
    db.run(
      `INSERT INTO orders (datetime, status, user_id)
      VALUES (?, ?, (SELECT id FROM users WHERE email = ?))`,
      [actualDateString(), "new", user_email],
      (err) => {
        if (err) reject(err);
        else resolve();
      }
    );
  });
};

const updateStatus = (id, newStatus) => {
  return new Promise((resolve, reject) => {
    db.run(
      "UPDATE orders SET status = ? WHERE id = ?",
      [newStatus, id],
      (err) => {
        if (err) reject(err);
        else resolve();
      }
    );
  });
};

module.exports = { createTable, add, getLastID, get, getAll, updateStatus };
