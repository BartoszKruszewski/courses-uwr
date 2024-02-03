const db = require("../database");

const createTable = () => {
  db.run(
    `CREATE TABLE IF NOT EXISTS 
    order_items
    (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      amount INTEGER NOT NULL,
      product_id INTEGER NOT NULL,
      order_id INTEGER NOT NULL,
      FOREIGN KEY (product_id) REFERENCES products(id),
      FOREIGN KEY (order_id) REFERENCES orders(id)
    )`
  );
};

const getAll = (order_id) => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT
        products.name AS name,
        products.price AS price,
        products.description AS description,
        categories.name AS category,
        order_items.amount AS amount
      FROM order_items
      JOIN products ON products.id = order_items.product_id
      JOIN categories ON products.category_id = categories.id
      `,
      [order_id],
      (err, order_items) => {
        if (err) reject(err);
        else resolve(order_items);
      }
    );
  });
};

const get = (order_id) => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT
        products.name AS name,
        products.price AS price,
        products.description AS description,
        categories.name AS category,
        order_items.amount AS amount
      FROM order_items
      JOIN products ON products.id = order_items.product_id
      JOIN categories ON products.category_id = categories.id
      WHERE order_items.order_id = ?
      `,
      [order_id],
      (err, order_items) => {
        if (err) reject(err);
        else resolve(order_items);
      }
    );
  });
};

const add = (amount, product_id, order_id) => {
  return new Promise((resolve, reject) => {
    db.run(
      `INSERT INTO order_items (amount, product_id, order_id)
      VALUES (?, ?, ?)`,
      [amount, product_id, order_id],
      (err) => {
        if (err) reject(err);
        else resolve();
      }
    );
  });
};

module.exports = { createTable, add, get, getAll };
