module.exports = (app, models) => {
  app.post("/addToCart", (req, res) => {
    const productID = req.body.addToCart;
    let cart = "";
    if (req.cookies.cart) cart = req.cookies.cart;
    res.cookie("cart", productID + ";" + cart);
    res.redirect("/");
  });
};
