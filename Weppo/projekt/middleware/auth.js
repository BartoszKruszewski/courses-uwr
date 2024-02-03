const crypto = require("crypto");
const config = require("../config");

module.exports = (app, models) => {
  app.use((req, res, next) => {
    const admin_paths = ["/cms"];
    const user_paths = ["/account", "/addToCart"];

    models.user.get(req.cookies.user).then((user) => {
      if (user) {
        const tokenHmac = crypto
          .createHmac("sha256", config.secret)
          .update(user.email + user.hmac)
          .digest("base64");
        if (req.cookies.auth_token === tokenHmac) {
          if (config.admins.includes(user.email)) {
            res.locals.user = req.cookies.user;
            res.locals.is_admin = true;
            next();
          } else {
            if (config.admins.includes(req.path))
              res.redirect("/login?returnUrl=" + req.path);
            else {
              res.locals.user = req.cookies.user;
              res.locals.is_admin = false;
              next();
            }
          }
        } else res.redirect("/login?returnUrl=" + req.path);
      } else if (
        !admin_paths.includes(req.path) &&
        !user_paths.includes(req.path)
      )
        next();
      else res.redirect("/login?returnUrl=" + req.path);
    });
  });
};
