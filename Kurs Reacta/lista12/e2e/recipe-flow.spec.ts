import { expect, test } from "@playwright/test";

test("user can add a recipe from the home screen", async ({ page }) => {
  await page.goto("/");

  await expect(page.getByRole("heading", { name: "Recipe Box" })).toBeVisible();

  await page.getByLabel("Title").fill("Brownies");
  await page.getByLabel("Content").fill("Mix cocoa, butter, and sugar.");
  await page.getByRole("button", { name: "Add recipe" }).click();

  await expect(page.getByRole("article", { name: "Recipe: Brownies" })).toBeVisible();
  await expect(page.getByText("Mix cocoa, butter, and sugar.")).toBeVisible();
});