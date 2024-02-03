const fs = require("fs");

function read(path) {
  fs.readFile(path, "utf8", (error, data) => {
    if (error) console.error(error);
    else console.log(data);
  });
}

read("lorem.txt");
