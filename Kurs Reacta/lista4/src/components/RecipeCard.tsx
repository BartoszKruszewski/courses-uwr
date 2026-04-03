import type { Recipe } from '../store/useRecipeStore'

type RecipeCardProps = {
  recipe: Recipe
  onRemove: (id: string) => void
  onToggleFavorite: (id: string) => void
}

export function RecipeCard({
  recipe,
  onRemove,
  onToggleFavorite,
}: RecipeCardProps) {
  return (
    <article className={`recipe-card ${recipe.isFavorite ? 'favorite' : ''}`}>
      <header>
        <h3>{recipe.title}</h3>
        <button
          type="button"
          className="btn icon"
          onClick={() => onToggleFavorite(recipe.id)}
          aria-label={recipe.isFavorite ? 'Usun z ulubionych' : 'Dodaj do ulubionych'}
          title={recipe.isFavorite ? 'Usun z ulubionych' : 'Dodaj do ulubionych'}
        >
          {recipe.isFavorite ? '★' : '☆'}
        </button>
      </header>

      <p>{recipe.content}</p>

      <footer>
        <button
          type="button"
          className="btn danger"
          onClick={() => onRemove(recipe.id)}
        >
          Usun
        </button>
      </footer>
    </article>
  )
}
