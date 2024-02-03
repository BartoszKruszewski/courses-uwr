const fs = require("fs");

function readFilePromise(filename, encoding) {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, encoding, (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

readFilePromise("lorem.txt", "utf8")
  .then((data) => console.log(data))
  .catch((err) => console.error(err));
