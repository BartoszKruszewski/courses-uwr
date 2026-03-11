import type { Recipe } from "../RecipeContext";
import { useRecipes } from "../RecipeContext";

interface Props {
  recipe: Recipe;
}

export default function RecipeCard({ recipe }: Props) {
  const { dispatch } = useRecipes();

  return (
    <div className={`recipe-card${recipe.favorite ? " favorite" : ""}`}>
      <div className="recipe-card-header">
        <h3>{recipe.title}</h3>
        <div className="recipe-card-actions">
          <button
            className="btn-fav"
            onClick={() =>
              dispatch({ type: "TOGGLE_FAVORITE", payload: { id: recipe.id } })
            }
            title={recipe.favorite ? "Remove from favorites" : "Mark as favorite"}
          >
            {recipe.favorite ? "★" : "☆"}
          </button>
          <button
            className="btn-delete"
            onClick={() =>
              dispatch({ type: "DELETE_RECIPE", payload: { id: recipe.id } })
            }
            title="Delete recipe"
          >
            ✕
          </button>
        </div>
      </div>
      <p>{recipe.content}</p>
    </div>
  );
}
