const fs = require("fs");
const path = require("path");

module.exports = (app, models) => {
  fs.readdirSync(__dirname).forEach((file) => {
    if (file.endsWith(".js") && file !== "index.js") {
      require(path.join(__dirname, file))(app, models);
    }
  });
};
