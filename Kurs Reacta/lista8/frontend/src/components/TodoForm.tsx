type TodoFormProps = {
  value: string
  onValueChange: (value: string) => void
  onSubmit: () => void
  disabled?: boolean
  isSubmitting?: boolean
}

export function TodoForm({
  value,
  onValueChange,
  onSubmit,
  disabled = false,
  isSubmitting = false,
}: TodoFormProps) {
  return (
    <form
      className="flex flex-col gap-3 rounded-3xl border border-white/10 bg-slate-950/60 p-4 shadow-2xl shadow-sky-950/20 backdrop-blur md:flex-row"
      onSubmit={(event) => {
        event.preventDefault()
        onSubmit()
      }}
    >
      <label className="flex-1">
        <span className="mb-2 block text-sm font-medium text-slate-300">
          Nowe zadanie
        </span>
        <input
          className="w-full rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-slate-100 outline-none transition placeholder:text-slate-500 focus:border-sky-400 focus:bg-white/10"
          placeholder="Np. odebrać zakupy"
          value={value}
          onChange={(event) => onValueChange(event.target.value)}
          disabled={disabled}
        />
      </label>
      <button
        type="submit"
        disabled={disabled || value.trim().length === 0}
        className="inline-flex items-center justify-center rounded-2xl bg-sky-400 px-5 py-3 font-semibold text-slate-950 transition hover:bg-sky-300 disabled:cursor-not-allowed disabled:bg-slate-700 disabled:text-slate-400"
      >
        {isSubmitting ? 'Dodawanie...' : 'Dodaj zadanie'}
      </button>
    </form>
  )
}