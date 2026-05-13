import type { TodoFilter } from '../api'

type TodoFiltersProps = {
  value: TodoFilter
  onChange: (value: TodoFilter) => void
  disabled?: boolean
}

const FILTERS: Array<{ value: TodoFilter; label: string }> = [
  { value: 'all', label: 'Wszystkie' },
  { value: 'active', label: 'Aktywne' },
  { value: 'done', label: 'Ukończone' },
]

export function TodoFilters({ value, onChange, disabled = false }: TodoFiltersProps) {
  return (
    <section className="flex flex-wrap items-center gap-3 rounded-3xl border border-white/10 bg-slate-950/55 p-4 shadow-2xl shadow-sky-950/10 backdrop-blur">
      <div className="text-sm font-medium text-slate-300">Filtr</div>
      <div className="flex flex-wrap gap-2">
        {FILTERS.map((filter) => (
          <button
            key={filter.value}
            type="button"
            onClick={() => onChange(filter.value)}
            disabled={disabled}
            aria-pressed={value === filter.value}
            className={`rounded-full border px-4 py-2 text-sm font-medium transition disabled:cursor-not-allowed disabled:opacity-60 ${
              value === filter.value
                ? 'border-sky-400 bg-sky-400 text-slate-950'
                : 'border-white/10 bg-white/5 text-slate-200 hover:border-sky-400/40 hover:bg-sky-400/10'
            }`}
          >
            {filter.label}
          </button>
        ))}
      </div>
    </section>
  )
}