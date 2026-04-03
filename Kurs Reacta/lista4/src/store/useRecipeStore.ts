import { create } from 'zustand'

export type Recipe = {
  id: string
  title: string
  content: string
  isFavorite: boolean
}

type RecipeState = {
  recipes: Recipe[]
  searchTerm: string
  showFavoritesOnly: boolean
  addRecipe: (title: string, content: string) => void
  removeRecipe: (id: string) => void
  toggleFavorite: (id: string) => void
  setSearchTerm: (value: string) => void
  setShowFavoritesOnly: (value: boolean) => void
}

const initialRecipes: Recipe[] = [
  {
    id: crypto.randomUUID(),
    title: 'Makaron aglio e olio',
    content:
      'Ugotuj makaron al dente, podsmaz czosnek na oliwie, dodaj chili i natke. Wymieszaj z makaronem i podawaj od razu.',
    isFavorite: true,
  },
  {
    id: crypto.randomUUID(),
    title: 'Owsianka z jablkiem',
    content:
      'Gotuj platki owsiane w mleku przez 5 minut. Dodaj starte jablko, cynamon i lyzeczke miodu.',
    isFavorite: false,
  },
]

export const useRecipeStore = create<RecipeState>((set) => ({
  recipes: initialRecipes,
  searchTerm: '',
  showFavoritesOnly: false,
  addRecipe: (title, content) =>
    set((state) => ({
      recipes: [
        {
          id: crypto.randomUUID(),
          title: title.trim(),
          content: content.trim(),
          isFavorite: false,
        },
        ...state.recipes,
      ],
    })),
  removeRecipe: (id) =>
    set((state) => ({
      recipes: state.recipes.filter((recipe) => recipe.id !== id),
    })),
  toggleFavorite: (id) =>
    set((state) => ({
      recipes: state.recipes.map((recipe) =>
        recipe.id === id
          ? { ...recipe, isFavorite: !recipe.isFavorite }
          : recipe,
      ),
    })),
  setSearchTerm: (value) => set({ searchTerm: value }),
  setShowFavoritesOnly: (value) => set({ showFavoritesOnly: value }),
}))
