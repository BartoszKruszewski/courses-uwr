const express = require("express");

const app = express();
const port = 3000;

app.set("view engine", "ejs");
app.set("views", "views");

app.get("/", (req, res) => {
  res.render("zad2_a");
});

app.listen(port, () => {
  console.log(`Serwer działa na http://localhost:${port}`);
});
