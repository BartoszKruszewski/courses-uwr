const fs = require("fs");
const util = require("util");

const readFilePromise = util.promisify(fs.readFile);

readFilePromise("lorem.txt", "utf8")
  .then((data) => console.log(data))
  .catch((err) => console.error(err));
