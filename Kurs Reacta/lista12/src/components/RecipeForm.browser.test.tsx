import "@vitest/browser/matchers";
import { afterEach, test, expect } from "vitest";
import { page, userEvent } from "vitest/browser";
import { cleanup, render } from "vitest-browser-react";
import { RecipeProvider } from "../context/RecipeContext";
import RecipeForm from "./RecipeForm";
import RecipeList from "./RecipeList";
afterEach(async () => {
  await cleanup();
});

test("shows validation error when submitted empty", async () => {
  await render(
    <RecipeProvider initialRecipes={[]}>
      <RecipeForm />
      <RecipeList />
    </RecipeProvider>,
  );

  await userEvent.click(page.getByRole("button", { name: "Add recipe" }));

  await expect.element(page.getByText("Title is required.")).toBeVisible();
  await expect.element(page.getByRole("status")).toHaveTextContent(
    "No recipes found.",
  );
});

test("adds a recipe and shows it in the list", async () => {
  await render(
    <RecipeProvider initialRecipes={[]}>
      <RecipeForm />
      <RecipeList />
    </RecipeProvider>,
  );

  await userEvent.fill(page.getByLabelText("Title"), "Brownies");
  await userEvent.fill(
    page.getByLabelText("Content"),
    "Mix cocoa, butter, and sugar.",
  );
  await userEvent.click(page.getByRole("button", { name: "Add recipe" }));

  await expect
    .element(page.getByRole("article", { name: "Recipe: Brownies" }))
    .toBeVisible();
  await expect
    .element(page.getByText("Mix cocoa, butter, and sugar."))
    .toBeVisible();
});