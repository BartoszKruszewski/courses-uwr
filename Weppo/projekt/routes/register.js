const crypto = require("crypto");
const secret = require("../config").secret;

module.exports = (app, models) => {
  app.get("/register", (req, res) => {
    let msg = "";
    if (req.query.msg) msg = req.query.msg.replace(/_/g, " ");
    res.render("index", {
      contentTemplate: "register",
      msg,
    });
  });

  app.post("/register", (req, res) => {
    const { email, password, confirmPassword } = req.body;
    if (password == confirmPassword) {
      const passHmac = crypto
        .createHmac("sha256", secret)
        .update(password)
        .digest("base64");
      models.user.add(email, passHmac);
      res.redirect("/login?returnPage=/");
    } else {
      res.redirect("/register?msg=The_passwords_are_not_the_same!");
    }
  });
};
