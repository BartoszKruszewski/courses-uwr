const express = require("express");
const cookieParser = require("cookie-parser");
const csurf = require("csurf");

const app = express();

app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

const csrfProtection = csurf({ cookie: true });

app.get("/", csrfProtection, (req, res) => {
  const csrfToken = req.csrfToken();
  res.cookie("XSRF-TOKEN", csrfToken);

  res.send(`<form action="/process" method="post">
                <input type="hidden" name="_csrf" value="${csrfToken}">
                <button type="submit">Submit</button>
              </form>`);
});

app.post("/process", csrfProtection, (req, res) => {
  if (req.body._csrf === req.cookies["XSRF-TOKEN"]) {
    res.send("Dane przetworzone poprawnie!");
  } else {
    res.status(403).send("Błąd CSRF. Żądanie odrzucone.");
  }
});

app.get("/process", csrfProtection, (req, res) => {
  if (req.body._csrf === req.cookies["XSRF-TOKEN"]) {
    res.send("Dane przetworzone poprawnie!");
  } else {
    res.status(403).send("Błąd CSRF. Żądanie odrzucone.");
  }
});

app.listen(3000, () => {
  console.log("Serwer działa na porcie 3000");
});
