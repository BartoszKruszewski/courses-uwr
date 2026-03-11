import { useState } from "react";
import { useRecipes } from "../RecipeContext";
import RecipeCard from "./RecipeCard";

export default function RecipeList() {
  const { recipes } = useRecipes();
  const [search, setSearch] = useState("");
  const [favoritesOnly, setFavoritesOnly] = useState(false);

  const keyword = search.toLowerCase();

  const filtered = recipes.filter((r) => {
    if (favoritesOnly && !r.favorite) return false;
    if (
      keyword &&
      !r.title.toLowerCase().includes(keyword) &&
      !r.content.toLowerCase().includes(keyword)
    )
      return false;
    return true;
  });

  return (
    <section className="recipe-list-section">
      <div className="filters">
        <input
          type="text"
          placeholder="Search recipes…"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="search-input"
        />
        <label className="fav-filter">
          <input
            type="checkbox"
            checked={favoritesOnly}
            onChange={(e) => setFavoritesOnly(e.target.checked)}
          />
          Favorites only
        </label>
      </div>

      {filtered.length === 0 ? (
        <p className="empty-message">No recipes found.</p>
      ) : (
        <div className="recipe-grid">
          {filtered.map((r) => (
            <RecipeCard key={r.id} recipe={r} />
          ))}
        </div>
      )}
    </section>
  );
}
