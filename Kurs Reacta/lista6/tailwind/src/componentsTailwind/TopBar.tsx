import { themes, type ThemeMode } from '../model'

function TopBar({
  theme,
  onThemeChange,
}: {
  theme: ThemeMode
  onThemeChange: (t: ThemeMode) => void
}) {
  return (
    <div className="flex items-center justify-between rounded-xl border border-slate-200 bg-white px-6 py-5 dark:border-slate-700 dark:bg-slate-800 midnight:border-[#3b2756] midnight:bg-[#261838]">
      <h1 className="m-0 text-base font-bold text-slate-900 dark:text-slate-100 midnight:text-violet-100">
        Theme Showcase
      </h1>
      <select
        className="cursor-pointer rounded-lg border border-slate-300 bg-slate-50 px-3 py-1.5 text-sm font-medium text-slate-700 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-400 dark:border-slate-600 dark:bg-slate-900 dark:text-slate-200 dark:focus:ring-indigo-400 midnight:border-violet-700 midnight:bg-[#1a1025] midnight:text-violet-200 midnight:focus:ring-violet-500"
        value={theme}
        onChange={(e) => onThemeChange(e.target.value as ThemeMode)}
      >
        {themes.map((t) => (
          <option key={t} value={t}>
            {t.charAt(0).toUpperCase() + t.slice(1)}
          </option>
        ))}
      </select>
    </div>
  )
}

export default TopBar
