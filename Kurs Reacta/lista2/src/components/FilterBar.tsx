interface FilterBarProps {
  searchTerm: string
  onSearchChange: (term: string) => void
  showOnlyActive: boolean
  onToggleShowOnlyActive: () => void
}

export function FilterBar({
  searchTerm,
  onSearchChange,
  showOnlyActive,
  onToggleShowOnlyActive,
}: FilterBarProps) {
  return (
    <div className="filter-bar">
      <div className="search-box">
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => onSearchChange(e.target.value)}
          placeholder="Search tasks..."
          className="search-input"
        />
      </div>
      <label className="toggle-label">
        <input
          type="checkbox"
          checked={showOnlyActive}
          onChange={onToggleShowOnlyActive}
          className="toggle-checkbox"
        />
        <span>Show only active</span>
      </label>
    </div>
  )
}
