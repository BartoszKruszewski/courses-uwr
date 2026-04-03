type RecipeFiltersProps = {
  searchTerm: string
  showFavoritesOnly: boolean
  onSearchTermChange: (value: string) => void
  onShowFavoritesOnlyChange: (value: boolean) => void
}

export function RecipeFilters({
  searchTerm,
  showFavoritesOnly,
  onSearchTermChange,
  onShowFavoritesOnlyChange,
}: RecipeFiltersProps) {
  return (
    <section className="card filters" aria-label="Filtry przepisow">
      <h2>Filtry</h2>
      <label className="field">
        <span>Szukaj po tytule lub tresci</span>
        <input
          value={searchTerm}
          onChange={(event) => onSearchTermChange(event.target.value)}
          placeholder="Np. makaron, cebula, deser..."
        />
      </label>

      <label className="favorite-toggle">
        <input
          type="checkbox"
          checked={showFavoritesOnly}
          onChange={(event) => onShowFavoritesOnlyChange(event.target.checked)}
        />
        Pokaz tylko ulubione
      </label>
    </section>
  )
}
