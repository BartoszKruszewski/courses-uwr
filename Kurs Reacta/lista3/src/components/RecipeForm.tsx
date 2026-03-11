import { useState, type FormEvent } from "react";
import { useRecipes } from "../RecipeContext";

export default function RecipeForm() {
  const { dispatch } = useRecipes();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    const trimmedTitle = title.trim();
    const trimmedContent = content.trim();
    if (!trimmedTitle || !trimmedContent) return;
    dispatch({
      type: "ADD_RECIPE",
      payload: { title: trimmedTitle, content: trimmedContent },
    });
    setTitle("");
    setContent("");
  };

  return (
    <form className="recipe-form" onSubmit={handleSubmit}>
      <h2>Add Recipe</h2>
      <input
        type="text"
        placeholder="Recipe title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Recipe content"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        rows={4}
      />
      <button type="submit">Add</button>
    </form>
  );
}
