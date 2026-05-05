import type { Dispatch, SetStateAction } from 'react'
import { useMemo } from 'react'
import { Combobox } from '@base-ui/react'
import { SettingsTooltip } from './SettingsTooltip'

export interface ComboboxOption<Value extends string = string> {
  label: string
  value: Value
}

export interface SettingsComboboxProps<Value extends string = string> {
  label: string
  options: readonly ComboboxOption<Value>[]
  onValueChange: Dispatch<SetStateAction<Value[]>>
  placeholder?: string
  tooltip?: string
  value: readonly Value[]
}

export function SettingsCombobox<Value extends string = string>({
  label,
  options,
  onValueChange,
  placeholder = 'Choose items',
  tooltip,
  value,
}: SettingsComboboxProps<Value>) {
  const labelsByValue = useMemo(
    () => new Map(options.map((option) => [option.value, option.label])),
    [options],
  )

  return (
    <div className="settings-field-shell settings-combobox-shell">
      <div className="settings-field-heading settings-combobox-heading">
        <div className="settings-label-row">
          <span className="settings-field-label">{label}</span>
          {tooltip ? (
            <SettingsTooltip content={tooltip} label={tooltip}>
              <span aria-hidden="true">i</span>
            </SettingsTooltip>
          ) : null}
        </div>
      </div>

      <Combobox.Root<Value, true>
        multiple
        items={options}
        value={value as Value[]}
        onValueChange={(next) => onValueChange(next)}
        autoHighlight
      >
        <Combobox.Trigger className="settings-combobox-trigger">
          <Combobox.Value placeholder={placeholder}>
            {(selectedValue: Value[]) => {
              if (selectedValue.length === 0) {
                return <span className="settings-combobox-placeholder">{placeholder}</span>
              }

              const visibleValues: Value[] = selectedValue.slice(0, 2)
              const hiddenCount = selectedValue.length - visibleValues.length

              return (
                <span className="settings-combobox-summary">
                  {visibleValues.map((selected) => (
                    <span key={selected} className="settings-combobox-chip">
                      {labelsByValue.get(selected) ?? selected}
                    </span>
                  ))}
                  {hiddenCount > 0 ? (
                    <span className="settings-combobox-more">+{hiddenCount}</span>
                  ) : null}
                </span>
              )
            }}
          </Combobox.Value>
          <span className="settings-combobox-chevron" aria-hidden="true">
            ▾
          </span>
        </Combobox.Trigger>

        <Combobox.Portal>
          <Combobox.Positioner className="settings-combobox-positioner" sideOffset={10}>
            <Combobox.Popup className="settings-combobox-popup">
              <div className="settings-combobox-input-row">
                <Combobox.Input
                  className="settings-combobox-input"
                  aria-label={`${label} filter`}
                  placeholder="Type to filter skills"
                />
                <Combobox.Status className="settings-combobox-status" />
              </div>

              <Combobox.Empty className="settings-combobox-empty">
                No matching skills.
              </Combobox.Empty>

              <Combobox.List className="settings-combobox-list">
                {(option: ComboboxOption<Value>) => (
                  <Combobox.Item
                    key={option.value}
                    value={option.value}
                    className="settings-combobox-item"
                  >
                    <span className="settings-combobox-item-text">{option.label}</span>
                    <Combobox.ItemIndicator className="settings-combobox-item-indicator">
                      ✓
                    </Combobox.ItemIndicator>
                  </Combobox.Item>
                )}
              </Combobox.List>
            </Combobox.Popup>
          </Combobox.Positioner>
        </Combobox.Portal>
      </Combobox.Root>
    </div>
  )
}