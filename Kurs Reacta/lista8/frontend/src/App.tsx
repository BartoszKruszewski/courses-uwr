import { useEffect, useMemo, useState } from 'react'
import { createTodo, deleteTodo, getTodos, updateTodo } from './api'
import { TodoForm } from './components/TodoForm'
import { TodoList } from './components/TodoList'
import type { Todo } from './types'

function App() {
  const [todos, setTodos] = useState<Todo[]>([])
  const [newTodoText, setNewTodoText] = useState('')
  const [loadingState, setLoadingState] = useState<{
    kind: 'load' | 'add' | 'toggle' | 'delete'
    todoId?: string
  } | null>(null)
  const [errorMessage, setErrorMessage] = useState<string | null>(null)

  const isBusy = loadingState !== null

  const loadingMessage = useMemo(() => {
    if (!loadingState) {
      return null
    }

    switch (loadingState.kind) {
      case 'load':
        return 'Ładowanie listy...'
      case 'add':
        return 'Dodawanie zadania...'
      case 'toggle':
        return 'Zapisywanie zmian...'
      case 'delete':
        return 'Usuwanie zadania...'
    }
  }, [loadingState])

  useEffect(() => {
    let isMounted = true

    async function loadTodos() {
      setLoadingState({ kind: 'load' })
      setErrorMessage(null)

      try {
        const todosFromApi = await getTodos()

        if (isMounted) {
          setTodos(todosFromApi)
        }
      } catch (error) {
        if (isMounted) {
          setErrorMessage(error instanceof Error ? error.message : 'Nie udało się pobrać zadań')
        }
      } finally {
        if (isMounted) {
          setLoadingState(null)
        }
      }
    }

    void loadTodos()

    return () => {
      isMounted = false
    }
  }, [])

  const completedCount = useMemo(
    () => todos.filter((todo) => todo.done).length,
    [todos],
  )

  const activeCount = todos.length - completedCount

  async function handleAddTodo() {
    const text = newTodoText.trim()

    if (!text || isBusy) {
      return
    }

    setErrorMessage(null)
    setLoadingState({ kind: 'add' })

    try {
      const createdTodo = await createTodo(text)
      setTodos((currentTodos) => [...currentTodos, createdTodo])
      setNewTodoText('')
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'Nie udało się dodać zadania')
    } finally {
      setLoadingState(null)
    }
  }

  async function handleToggleTodo(todo: Todo) {
    if (isBusy) {
      return
    }

    setErrorMessage(null)
    setLoadingState({ kind: 'toggle', todoId: todo.id })

    try {
      const updatedTodo = await updateTodo(todo.id, {
        text: todo.text,
        done: !todo.done,
      })

      setTodos((currentTodos) =>
        currentTodos.map((currentTodo) =>
          currentTodo.id === updatedTodo.id ? updatedTodo : currentTodo,
        ),
      )
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'Nie udało się zmienić zadania')
    } finally {
      setLoadingState(null)
    }
  }

  async function handleDeleteTodo(id: string) {
    if (isBusy) {
      return
    }

    setErrorMessage(null)
    setLoadingState({ kind: 'delete', todoId: id })

    try {
      await deleteTodo(id)
      setTodos((currentTodos) => currentTodos.filter((todo) => todo.id !== id))
    } catch (error) {
      setErrorMessage(error instanceof Error ? error.message : 'Nie udało się usunąć zadania')
    } finally {
      setLoadingState(null)
    }
  }

  return (
    <main className="min-h-screen px-4 py-10 text-slate-100 sm:px-6 lg:px-8">
      <section className="mx-auto flex w-full max-w-4xl flex-col gap-6">
        <header className="rounded-[2rem] border border-white/10 bg-slate-950/60 p-6 shadow-2xl shadow-sky-950/20 backdrop-blur md:p-8">
          <div className="flex flex-col gap-4 lg:flex-row lg:items-end lg:justify-between">
            <div className="space-y-3">
              <p className="inline-flex rounded-full border border-sky-400/20 bg-sky-400/10 px-3 py-1 text-xs font-semibold uppercase tracking-[0.32em] text-sky-200">
                React + API
              </p>
              <div className="space-y-2">
                <h1 className="balance-text text-4xl font-semibold tracking-tight text-white sm:text-5xl">
                  ToDo lista z podpiętym REST API
                </h1>
                <p className="max-w-2xl text-sm leading-6 text-slate-300 sm:text-base">
                  Dodawaj zadania, przełączaj ich status i usuwaj je bezpośrednio
                  z backendu na <span className="text-sky-200">localhost:3001</span>.
                </p>
              </div>
            </div>

            <div className="grid grid-cols-3 gap-3 text-center text-sm">
              <div className="rounded-2xl border border-white/10 bg-white/5 px-4 py-3">
                <div className="text-2xl font-semibold text-white">{todos.length}</div>
                <div className="text-slate-400">Wszystkie</div>
              </div>
              <div className="rounded-2xl border border-emerald-400/20 bg-emerald-400/10 px-4 py-3">
                <div className="text-2xl font-semibold text-emerald-300">{completedCount}</div>
                <div className="text-slate-300">Done</div>
              </div>
              <div className="rounded-2xl border border-amber-400/20 bg-amber-400/10 px-4 py-3">
                <div className="text-2xl font-semibold text-amber-200">{activeCount}</div>
                <div className="text-slate-300">Aktywne</div>
              </div>
            </div>
          </div>
        </header>

        {errorMessage ? (
          <div className="rounded-3xl border border-rose-400/20 bg-rose-400/10 px-4 py-3 text-sm text-rose-100">
            {errorMessage}
          </div>
        ) : null}

        {loadingMessage ? (
          <div className="rounded-3xl border border-sky-400/20 bg-sky-400/10 px-4 py-3 text-sm text-sky-100">
            {loadingMessage}
          </div>
        ) : null}

        <TodoForm
          value={newTodoText}
          onValueChange={setNewTodoText}
          onSubmit={handleAddTodo}
          disabled={isBusy}
          isSubmitting={loadingState?.kind === 'add'}
        />

        <section className="rounded-[2rem] border border-white/10 bg-slate-950/50 p-4 shadow-2xl shadow-sky-950/10 backdrop-blur md:p-6">
          {loadingState?.kind === 'load' ? (
            <div className="flex min-h-48 items-center justify-center rounded-3xl border border-dashed border-white/10 bg-white/5 text-slate-300">
              Ładowanie...
            </div>
          ) : todos.length === 0 ? (
            <div className="flex min-h-48 flex-col items-center justify-center rounded-3xl border border-dashed border-white/10 bg-white/5 px-6 text-center text-slate-300">
              <p className="text-lg font-medium text-white">Brak zadań</p>
              <p className="mt-2 max-w-md text-sm leading-6 text-slate-400">
                Dodaj pierwsze zadanie powyżej. Lista automatycznie zapisze się w API.
              </p>
            </div>
          ) : (
            <TodoList
              todos={todos}
              onToggle={handleToggleTodo}
              onDelete={handleDeleteTodo}
              disabled={isBusy}
              busyTodoId={loadingState?.todoId ?? null}
              busyAction={
                loadingState?.kind === 'toggle' || loadingState?.kind === 'delete'
                  ? loadingState.kind
                  : null
              }
            />
          )}
        </section>
      </section>
    </main>
  )
}

export default App
