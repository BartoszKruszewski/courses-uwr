import { useState } from 'react'
import type { FormEvent } from 'react'

type RecipeFormProps = {
  onAddRecipe: (title: string, content: string) => void
}

export function RecipeForm({ onAddRecipe }: RecipeFormProps) {
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()

    const normalizedTitle = title.trim()
    const normalizedContent = content.trim()

    if (!normalizedTitle || !normalizedContent) {
      return
    }

    onAddRecipe(normalizedTitle, normalizedContent)
    setTitle('')
    setContent('')
  }

  return (
    <form className="card recipe-form" onSubmit={handleSubmit}>
      <h2>Dodaj nowy przepis</h2>
      <label className="field">
        <span>Tytul</span>
        <input
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          placeholder="Np. Zupa pomidorowa"
          maxLength={80}
        />
      </label>

      <label className="field">
        <span>Tresc przepisu</span>
        <textarea
          value={content}
          onChange={(event) => setContent(event.target.value)}
          placeholder="Opisz skladniki i kroki przygotowania..."
          rows={4}
          maxLength={600}
        />
      </label>

      <button type="submit" className="btn primary">
        Dodaj przepis
      </button>
    </form>
  )
}
