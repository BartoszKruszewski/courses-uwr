const express = require("express");
const multer = require("multer");
const cookieParser = require("cookie-parser");
const bodyParser = require("body-parser");
const path = require("path");
const { db, models } = require("./database");

const app = express();

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(cookieParser());

const storage = multer.diskStorage({
  destination: "./public/uploads/",
  filename: (req, file, cb) => {
    cb(null, file.fieldname + "-" + req.body.name + ".png");
  },
});

const upload = multer({ storage });

const middleware = require("./middleware")(app, models, upload);
const routes = require("./routes")(app, models, upload);

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
