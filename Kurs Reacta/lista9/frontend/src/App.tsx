import { useState } from 'react'
import type { TodoFilter } from './api'
import { TodoForm } from './components/TodoForm'
import { TodoFilters } from './components/TodoFilters'
import { TodoList } from './components/TodoList'
import { useCreateTodoMutation } from './hooks/useCreateTodoMutation'
import { useDeleteTodoMutation } from './hooks/useDeleteTodoMutation'
import { useTodosQuery } from './hooks/useTodosQuery'
import { useUpdateTodoMutation } from './hooks/useUpdateTodoMutation'
import type { Todo } from './types'

function getErrorMessage(error: unknown, fallbackMessage: string) {
  return error instanceof Error ? error.message : fallbackMessage
}

function App() {
  const [newTodoText, setNewTodoText] = useState('')
  const [filter, setFilter] = useState<TodoFilter>('all')

  const todosQuery = useTodosQuery()
  const createTodoMutation = useCreateTodoMutation()
  const updateTodoMutation = useUpdateTodoMutation()
  const deleteTodoMutation = useDeleteTodoMutation()

  const allTodos = todosQuery.data ?? []
  const todos =
    filter === 'done'
      ? allTodos.filter((todo) => todo.done)
      : filter === 'active'
        ? allTodos.filter((todo) => !todo.done)
        : allTodos
  const isMutating =
    createTodoMutation.isPending ||
    updateTodoMutation.isPending ||
    deleteTodoMutation.isPending

  const loadingMessage = todosQuery.isPending
    ? 'Ładowanie listy...'
    : todosQuery.isFetching
      ? 'Odświeżanie listy...'
      : null

  const queryErrorMessage = todosQuery.isError
    ? getErrorMessage(todosQuery.error, 'Nie udało się pobrać zadań')
    : null

  const mutationErrorMessage =
    getErrorMessage(createTodoMutation.error, '') ||
    getErrorMessage(updateTodoMutation.error, '') ||
    getErrorMessage(deleteTodoMutation.error, '') ||
    null

  const completedCount = allTodos.filter((todo) => todo.done).length
  const activeCount = allTodos.length - completedCount

  async function handleAddTodo() {
    const text = newTodoText.trim()

    if (!text || isMutating) {
      return
    }

    try {
      await createTodoMutation.mutateAsync(text)
      setNewTodoText('')
    } catch {
      return
    }
  }

  async function handleToggleTodo(todo: Todo) {
    if (isMutating) {
      return
    }

    try {
      await updateTodoMutation.mutateAsync({
        id: todo.id,
        todo: {
          text: todo.text,
          done: !todo.done,
        },
      })
    } catch {
      return
    }
  }

  async function handleDeleteTodo(id: string) {
    if (isMutating) {
      return
    }

    try {
      await deleteTodoMutation.mutateAsync(id)
    } catch {
      return
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
                <div className="text-2xl font-semibold text-white">{allTodos.length}</div>
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

        <TodoFilters value={filter} onChange={setFilter} disabled={isMutating} />

        {queryErrorMessage ? (
          <div className="rounded-3xl border border-rose-400/20 bg-rose-400/10 px-4 py-3 text-sm text-rose-100">
            {queryErrorMessage}
          </div>
        ) : null}

        {mutationErrorMessage ? (
          <div className="rounded-3xl border border-amber-400/20 bg-amber-400/10 px-4 py-3 text-sm text-amber-100">
            {mutationErrorMessage}
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
          disabled={isMutating || todosQuery.isPending}
          isSubmitting={createTodoMutation.isPending}
        />

        <section className="rounded-[2rem] border border-white/10 bg-slate-950/50 p-4 shadow-2xl shadow-sky-950/10 backdrop-blur md:p-6">
          {todosQuery.isPending ? (
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
              disabled={isMutating}
              busyTodoId={updateTodoMutation.variables?.id ?? deleteTodoMutation.variables ?? null}
              busyAction={
                updateTodoMutation.isPending
                  ? 'toggle'
                  : deleteTodoMutation.isPending
                    ? 'delete'
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
