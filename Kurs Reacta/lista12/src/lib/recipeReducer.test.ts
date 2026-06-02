import { test, expect, vi } from "vitest";
import { getRandomUUID } from "./getRandomUUID";
import { recipeReducer } from "./recipeReducer";
import type { Recipe } from "./recipe.types";

vi.mock("./getRandomUUID", () => ({
  getRandomUUID: vi.fn(() => "recipe-fixed-uuid"),
}));

test("adds a new recipe with a generated id", () => {
  const state: Recipe[] = [];

  const nextState = recipeReducer(state, {
    type: "ADD_RECIPE",
    payload: {
      title: "Brownies",
      content: "Mix cocoa, butter, and sugar.",
    },
  });

  expect(nextState).toEqual([
    {
      id: "recipe-fixed-uuid",
      title: "Brownies",
      content: "Mix cocoa, butter, and sugar.",
      isFavorite: false,
    },
  ]);
  expect(vi.mocked(getRandomUUID)).toHaveBeenCalledTimes(1);
});

test("deletes the matching recipe", () => {
  const state: Recipe[] = [
    {
      id: "recipe-1",
      title: "Brownies",
      content: "Mix cocoa, butter, and sugar.",
      isFavorite: false,
    },
    {
      id: "recipe-2",
      title: "Salad",
      content: "Toss lettuce and tomato.",
      isFavorite: true,
    },
  ];

  const nextState = recipeReducer(state, {
    type: "DELETE_RECIPE",
    payload: { id: "recipe-1" },
  });

  expect(nextState).toEqual([
    {
      id: "recipe-2",
      title: "Salad",
      content: "Toss lettuce and tomato.",
      isFavorite: true,
    },
  ]);
});

test("toggles the favorite flag for one recipe", () => {
  const state: Recipe[] = [
    {
      id: "recipe-1",
      title: "Brownies",
      content: "Mix cocoa, butter, and sugar.",
      isFavorite: false,
    },
    {
      id: "recipe-2",
      title: "Salad",
      content: "Toss lettuce and tomato.",
      isFavorite: true,
    },
  ];

  const nextState = recipeReducer(state, {
    type: "TOGGLE_FAVORITE",
    payload: { id: "recipe-2" },
  });

  expect(nextState).toEqual([
    {
      id: "recipe-1",
      title: "Brownies",
      content: "Mix cocoa, butter, and sugar.",
      isFavorite: false,
    },
    {
      id: "recipe-2",
      title: "Salad",
      content: "Toss lettuce and tomato.",
      isFavorite: false,
    },
  ]);
});