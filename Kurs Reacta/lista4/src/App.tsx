import { useMemo } from 'react'
import './App.css'
import { RecipeFilters } from './components/RecipeFilters'
import { RecipeForm } from './components/RecipeForm'
import { RecipeList } from './components/RecipeList'
import { useRecipeStore } from './store/useRecipeStore'

function App() {
  const recipes = useRecipeStore((state) => state.recipes)
  const searchTerm = useRecipeStore((state) => state.searchTerm)
  const showFavoritesOnly = useRecipeStore((state) => state.showFavoritesOnly)
  const addRecipe = useRecipeStore((state) => state.addRecipe)
  const removeRecipe = useRecipeStore((state) => state.removeRecipe)
  const toggleFavorite = useRecipeStore((state) => state.toggleFavorite)
  const setSearchTerm = useRecipeStore((state) => state.setSearchTerm)
  const setShowFavoritesOnly = useRecipeStore(
    (state) => state.setShowFavoritesOnly,
  )

  const filteredRecipes = useMemo(() => {
    const keyword = searchTerm.trim().toLowerCase()

    return recipes.filter((recipe) => {
      const matchesFavoriteFilter = showFavoritesOnly ? recipe.isFavorite : true

      if (!keyword) {
        return matchesFavoriteFilter
      }

      const inTitle = recipe.title.toLowerCase().includes(keyword)
      const inContent = recipe.content.toLowerCase().includes(keyword)

      return matchesFavoriteFilter && (inTitle || inContent)
    })
  }, [recipes, searchTerm, showFavoritesOnly])

  return (
    <main className="app">
      <header className="app-header">
        <p className="eyebrow">Lista 4 · Zustand</p>
        <h1>Ksiazka Kucharska</h1>
        <p>
          Dodawaj przepisy, oznaczaj ulubione i filtruj wyniki po slowach
          kluczowych.
        </p>
      </header>

      <section className="layout">
        <div className="sidebar">
          <RecipeForm onAddRecipe={addRecipe} />
          <RecipeFilters
            searchTerm={searchTerm}
            showFavoritesOnly={showFavoritesOnly}
            onSearchTermChange={setSearchTerm}
            onShowFavoritesOnlyChange={setShowFavoritesOnly}
          />
        </div>

        <div className="content">
          <div className="list-header">
            <h2>Przepisy</h2>
            <span>{filteredRecipes.length} wynikow</span>
          </div>
          <RecipeList
            recipes={filteredRecipes}
            onRemove={removeRecipe}
            onToggleFavorite={toggleFavorite}
          />
        </div>
      </section>
    </main>
  )
}

export default App
