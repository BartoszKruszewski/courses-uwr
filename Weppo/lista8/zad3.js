const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();
const port = 3000;

app.get("/", (req, res) => {
  // utworzenie pliku
  const csvData =
    "Id,Name,Email\n" +
    "1,John Doe,john@example.com\n" +
    "2,Jane Doe,jane@example.com";
  const fileName = "example.csv";
  fs.writeFileSync(fileName, csvData);

  // wyslanie pliku
  res.setHeader("Content-Disposition", `attachment; filename=${fileName}`);
  res.setHeader("Content-Type", "text/csv");
  res.send(fs.readFileSync(fileName));

  // usuniecie pliku
  fs.unlinkSync(fileName);
});

app.listen(port, () => {
  console.log(`Serwer działa na http://localhost:${port}`);
});
