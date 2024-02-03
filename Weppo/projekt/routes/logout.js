module.exports = (app, models) => {
  app.get("/logout", (req, res) => {
    res.clearCookie("auth_token");
    res.clearCookie("user");
    res.redirect("/");
  });
};
