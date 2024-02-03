const db = require("../database");

const createTable = () => {
  db.run(
    `CREATE TABLE IF NOT EXISTS 
    products
    (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT UNIQUE NOT NULL,
      description TEXT,
      price REAL NOT NULL,
      category_id INTEGER,
      FOREIGN KEY (category_id) REFERENCES categories(id)
    )`
  );
};

const getAll = () => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT
        products.id AS id,
        products.name AS name,
        products.description AS description,
        products.price AS price,
        categories.name AS category
      FROM products
      JOIN categories ON products.category_id = categories.id`,
      (err, products) => {
        if (err) reject(err);
        else resolve(products);
      }
    );
  });
};

const getByCategory = (category) => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT
        products.id AS id,
        products.name AS name,
        products.description AS description,
        products.price AS price,
        categories.name AS category
      FROM products
      JOIN categories ON products.category_id = categories.id
      WHERE categories.name LIKE '%${category}%'`,
      (err, products) => {
        if (err) reject(err);
        else resolve(products);
      }
    );
  });
};

const get = (search) => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT
        products.id AS id,
        products.name AS name,
        products.description AS description,
        products.price AS price,
        categories.name AS category
      FROM products
      JOIN categories ON products.category_id = categories.id
      WHERE products.name LIKE '%${search}%'`,
      (err, products) => {
        if (err) reject(err);
        else resolve(products);
      }
    );
  });
};

const getById = (ids) => {
  return new Promise((resolve, reject) => {
    db.all(
      `SELECT
        products.id AS id,
        products.name AS name,
        products.description AS description,
        products.price AS price,
        categories.name AS category
      FROM products
      JOIN categories ON products.category_id = categories.id
      WHERE products.id IN (${ids.map(() => "?").join(", ")})
      `,
      ids,
      (err, products) => {
        if (err) reject(err);
        else resolve(products);
      }
    );
  });
};

const add = (name, description, price, category_id) => {
  return new Promise((resolve, reject) => {
    db.run(
      `INSERT INTO products (name, description, price, category_id)
      VALUES (?, ?, ?, ?)`,
      [name, description, price, category_id],
      (err) => {
        if (err) reject(err);
        else resolve();
      }
    );
  });
};

module.exports = { createTable, get, getById, getAll, getByCategory, add };
