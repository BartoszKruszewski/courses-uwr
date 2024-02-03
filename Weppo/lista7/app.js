const http = require("http");
const express = require("express");
const app = express();

app.set("view engine", "ejs");
app.set("views", "./views");

app.use(express.urlencoded({ extended: true }));

app.post("/", (req, res) => {
  let { firstName, lastName, course, ...tasks } = req.body;
  let query = `?firstName=${firstName}&lastName=${lastName}&course=${course}&tasks=`;
  for (let value of Object.values(tasks)) query += `${value};`;
  console.log(query);
  res.redirect("/print" + query);
});

app.get("/", (req, res) => {
  res.render("form");
});

app.get("/print", (req, res) => {
  res.render("print", {
    firstName: req.query.firstName,
    lastName: req.query.lastName,
    course: req.query.course,
    tasks: req.query.tasks.split(";"),
  });
});

http.createServer(app).listen(3000);
console.log("Server started");
