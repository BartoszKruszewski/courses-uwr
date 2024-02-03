const express = require("express");
const multer = require("multer");
const path = require("path");

const app = express();
const port = 3000;

const storage = multer.diskStorage({
  destination: "uploads/",
  filename: (req, file, cb) => {
    cb(
      null,
      file.fieldname + "-" + Date.now() + path.extname(file.originalname)
    );
  },
});

const upload = multer({ storage });

app.set("view engine", "ejs");
app.set("views", "views");

app.get("/", (req, res) => {
  res.render("zad1");
});

app.post("/upload", upload.single("fileToUpload"), (req, res) => {
  res.send("Plik został pomyślnie przesłany!");
});

app.listen(port, () => {
  console.log(`Serwer działa na http://localhost:${port}`);
});
