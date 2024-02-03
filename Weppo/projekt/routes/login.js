const crypto = require("crypto");
const secret = require("../config").secret;

module.exports = (app, models) => {
  app.get("/login", (req, res) => {
    let msg = "";
    if (req.query.msg) msg = req.query.msg.replace(/_/g, " ");
    res.render("index", {
      contentTemplate: "login",
      msg,
    });
  });

  app.post("/login", (req, res) => {
    const returnPath = req.query.returnPath;
    const { email, password } = req.body;
    models.user.get(email).then((user) => {
      const passHmac = crypto
        .createHmac("sha256", secret)
        .update(password)
        .digest("base64");
      if (user && user.hmac == passHmac) {
        const tokenHmac = crypto
          .createHmac("sha256", secret)
          .update(email + passHmac)
          .digest("base64");
        res.cookie("auth_token", tokenHmac);
        res.cookie("user", email);
        if (returnPath) res.redirect(returnPath);
        else res.redirect("/");
      } else {
        res.redirect("/login?msg=Invalid_email_or_password!");
      }
    });
  });
};
