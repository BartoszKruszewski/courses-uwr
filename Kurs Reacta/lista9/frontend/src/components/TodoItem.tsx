import type { Todo } from '../types'

type TodoItemProps = {
  todo: Todo
  onToggle: (todo: Todo) => void
  onDelete: (id: string) => void
  disabled?: boolean
  isSaving?: boolean
  isDeleting?: boolean
}

export function TodoItem({
  todo,
  onToggle,
  onDelete,
  disabled = false,
  isSaving = false,
  isDeleting = false,
}: TodoItemProps) {
  return (
    <li
      className="flex flex-col gap-4 rounded-3xl border border-white/10 bg-white/5 p-4 transition hover:border-sky-400/40 hover:bg-white/7 md:flex-row md:items-center md:justify-between"
      aria-busy={isSaving || isDeleting}
    >
      <button
        type="button"
        onClick={() => onToggle(todo)}
        disabled={disabled}
        className="flex flex-1 items-start gap-3 text-left disabled:cursor-not-allowed"
      >
        <span
          className={`mt-1 inline-flex h-5 w-5 shrink-0 items-center justify-center rounded-full border transition ${
            todo.done
              ? 'border-emerald-400 bg-emerald-400 text-slate-950'
              : 'border-slate-500 text-transparent'
          }`}
        >
          ✓
        </span>
        <span className="space-y-1">
          <span
            className={`block text-lg font-medium transition ${
              todo.done ? 'text-slate-400 line-through' : 'text-slate-100'
            }`}
          >
            {todo.text}
          </span>
          <span className="block text-sm text-slate-400">
            {todo.done ? 'Zadanie ukończone' : 'Zadanie aktywne'}
          </span>
        </span>
      </button>

      <div className="flex items-center gap-3 self-start md:self-center">
        <button
          type="button"
          onClick={() => onToggle(todo)}
          disabled={disabled}
          className="rounded-2xl border border-white/10 px-4 py-2 text-sm font-medium text-slate-200 transition hover:border-sky-400/50 hover:bg-sky-400/10 disabled:cursor-not-allowed disabled:text-slate-500"
        >
          {isSaving ? 'Zapisywanie...' : todo.done ? 'Oznacz jako aktywne' : 'Oznacz jako done'}
        </button>
        <button
          type="button"
          onClick={() => onDelete(todo.id)}
          disabled={disabled}
          className="rounded-2xl border border-rose-400/20 px-4 py-2 text-sm font-medium text-rose-200 transition hover:bg-rose-400/10 disabled:cursor-not-allowed disabled:text-slate-500"
        >
          {isDeleting ? 'Usuwanie...' : 'Usuń'}
        </button>
      </div>
    </li>
  )
}