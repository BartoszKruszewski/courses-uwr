import type { Recipe } from '../store/useRecipeStore'
import { RecipeCard } from './RecipeCard'

type RecipeListProps = {
  recipes: Recipe[]
  onRemove: (id: string) => void
  onToggleFavorite: (id: string) => void
}

export function RecipeList({
  recipes,
  onRemove,
  onToggleFavorite,
}: RecipeListProps) {
  if (recipes.length === 0) {
    return (
      <section className="card empty-state" aria-live="polite">
        Brak przepisow pasujacych do aktualnych filtrow.
      </section>
    )
  }

  return (
    <section className="recipe-grid" aria-label="Lista przepisow">
      {recipes.map((recipe) => (
        <RecipeCard
          key={recipe.id}
          recipe={recipe}
          onRemove={onRemove}
          onToggleFavorite={onToggleFavorite}
        />
      ))}
    </section>
  )
}
