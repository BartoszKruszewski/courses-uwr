import { useState, useMemo } from 'react'
import './App.css'
import type { Todo } from './types'
import { TodoForm } from './components/TodoForm'
import { TodoList } from './components/TodoList'
import { FilterBar } from './components/FilterBar'

function App() {
  const [todos, setTodos] = useState<Todo[]>([])
  const [searchTerm, setSearchTerm] = useState('')
  const [showOnlyActive, setShowOnlyActive] = useState(false)

  const addTodo = (text: string) => {
    const newTodo: Todo = {
      id: Date.now().toString(),
      text,
      completed: false,
    }
    setTodos([...todos, newTodo])
  }

  const toggleTodo = (id: string) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    )
  }

  const deleteTodo = (id: string) => {
    setTodos(todos.filter((todo) => todo.id !== id))
  }

  const filteredTodos = useMemo(() => {
    return todos.filter((todo) => {
      const matchesSearch = todo.text
        .toLowerCase()
        .includes(searchTerm.toLowerCase())
      const matchesFilter = showOnlyActive ? !todo.completed : true
      return matchesSearch && matchesFilter
    })
  }, [todos, searchTerm, showOnlyActive])

  return (
    <div className="app-container">
      <header className="app-header">
        <h1 className="app-title">My Todo List</h1>
        <p className="app-subtitle">Manage your tasks efficiently</p>
      </header>

      <main className="app-main">
        <section className="todo-section">
          <div className="controls-wrapper">
            <TodoForm onAddTodo={addTodo} />
            <FilterBar
              searchTerm={searchTerm}
              onSearchChange={setSearchTerm}
              showOnlyActive={showOnlyActive}
              onToggleShowOnlyActive={() => setShowOnlyActive(!showOnlyActive)}
            />
          </div>
          <TodoList
            todos={filteredTodos}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
          />
        </section>
      </main>
    </div>
  )
}

export default App
