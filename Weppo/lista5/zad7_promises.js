const fs = require("fs").promises;

async function readFileAsync(filename, encoding) {
  try {
    const data = await fs.readFile(filename, encoding);
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}

readFileAsync("lorem.txt", "utf8");
