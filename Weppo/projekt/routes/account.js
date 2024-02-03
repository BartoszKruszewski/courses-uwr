module.exports = (app, models) => {
  app.get("/account", (req, res) => {
    let cart = "";
    if (req.cookies.cart) cart = req.cookies.cart;
    models.product.getById(cart.split(";")).then((products) => {
      let countedProducts = products.map((product) => ({
        ...product,
        amount: cart
          .split(";")
          .reduce((i, id) => (id === String(product.id) ? i + 1 : i), 0),
      }));
      models.order.get(req.cookies.user).then((orders) => {
        const promises = orders.map(
          (order) =>
            new Promise((resolve, reject) => {
              models.orderItem.get(order.id).then((orderItems) => {
                resolve({
                  ...order,
                  items: orderItems,
                  totalPrice: orderItems.reduce(
                    (suma, element) => suma + element.price * element.amount,
                    0
                  ),
                });
              });
            })
        );
        Promise.all(promises).then((ordersInfo) => {
          res.render("index", {
            contentTemplate: "account",
            cart: countedProducts,
            orders: ordersInfo,
          });
        });
      });
    });
  });

  app.post("/account", (req, res) => {
    let cart = "";
    if (req.cookies.cart) {
      cart = req.cookies.cart;
      res.clearCookie("cart");
    }
    models.product.getById(cart.split(";")).then((products) => {
      let countedProducts = products.map((product) => ({
        ...product,
        amount: cart
          .split(";")
          .reduce((i, id) => (id === String(product.id) ? i + 1 : i), 0),
      }));
      models.order.add(req.cookies.user);
      models.order.getLastID().then((order_id) => {
        countedProducts.forEach((product) => {
          models.orderItem.add(product.amount, product.id, order_id);
        });
      });
      res.redirect("/account");
    });
  });
};
