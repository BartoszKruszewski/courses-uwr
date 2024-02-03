module.exports = (app, models) => {
  app.get("/", (req, res) => {
    const { search, categorySearch } = req.query;
    models.category.get().then((categories) => {
      if (search)
        models.product.get(search).then((products) => {
          res.render("index", {
            contentTemplate: "home",
            products,
            categories,
          });
        });
      else if (categorySearch)
        models.product.getByCategory(categorySearch).then((products) => {
          res.render("index", {
            contentTemplate: "home",
            products,
            categories,
          });
        });
      else
        models.product.getAll().then((products) => {
          res.render("index", {
            contentTemplate: "home",
            products,
            categories,
          });
        });
    });
  });
};
