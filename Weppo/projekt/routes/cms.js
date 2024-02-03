module.exports = (app, models, upload) => {
  app.get("/cms", (req, res) => {
    models.user.getAll().then((users) => {
      models.category.get().then((categories) => {
        models.order.getAll().then((orders) => {
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
              contentTemplate: "cms",
              orders: ordersInfo,
              categories: categories,
              users: users,
            });
          });
        });
      });
    });
  });

  app.post("/cms", upload.single("image"), (req, res) => {
    const { type, name, description, price, category, orderID, orderStatus } =
      req.body;
    if (type == "product") {
      models.product.add(name, description, price, category);
    } else if (type == "category") models.category.add(name);
    else if (type == "order") models.order.updateStatus(orderID, orderStatus);
    res.redirect("/cms");
  });
};
