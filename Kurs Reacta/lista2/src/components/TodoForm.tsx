import { useState } from 'react'

interface TodoFormProps {
  onAddTodo: (text: string) => void
}

export function TodoForm({ onAddTodo }: TodoFormProps) {
  const [input, setInput] = useState('')

  return (
    <form
      className="todo-form"
      onSubmit={(e) => {
        e.preventDefault()
        if (input.trim()) {
          onAddTodo(input.trim())
          setInput('')
        }
      }}
    >
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Add a new task..."
        className="todo-input"
      />
      <button type="submit" className="add-button">
        Add
      </button>
    </form>
  )
}
