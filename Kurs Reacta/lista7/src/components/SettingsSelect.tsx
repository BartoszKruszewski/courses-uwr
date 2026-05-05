import type { Dispatch, SetStateAction } from 'react'
import { Select } from '@base-ui/react'

export interface SelectOption<Value extends string = string> {
  label: string
  value: Value
}

export interface SettingsSelectProps<Value extends string = string> {
  description?: string
  label: string
  onValueChange: Dispatch<SetStateAction<Value>>
  options: readonly SelectOption<Value>[]
  placeholder?: string
  value: Value
}

export function SettingsSelect<Value extends string = string>({
  description,
  label,
  onValueChange,
  options,
  placeholder = 'Select an option',
  value,
}: SettingsSelectProps<Value>) {
  return (
    <div className="settings-field-shell">
      <div className="settings-field-heading">
        <span className="settings-field-label">{label}</span>
        {description ? <span className="settings-field-description">{description}</span> : null}
      </div>

      <Select.Root<Value>
        items={options}
        value={value}
        onValueChange={(next) => {
          if (next != null) {
            onValueChange(next)
          }
        }}
      >
        <Select.Trigger className="settings-select-trigger">
          <Select.Value placeholder={placeholder} />
          <span className="settings-select-chevron" aria-hidden="true">
            ▾
          </span>
        </Select.Trigger>

        <Select.Portal>
          <Select.Backdrop className="settings-select-backdrop" />
          <Select.Positioner className="settings-select-positioner" sideOffset={10}>
            <Select.Popup className="settings-select-popup">
              <Select.List className="settings-select-list">
                {options.map((option) => (
                  <Select.Item
                    key={option.value}
                    value={option.value}
                    label={option.label}
                    className="settings-select-item"
                  >
                    <Select.ItemText className="settings-select-item-text">
                      {option.label}
                    </Select.ItemText>
                    <Select.ItemIndicator className="settings-select-item-indicator">
                      ✓
                    </Select.ItemIndicator>
                  </Select.Item>
                ))}
              </Select.List>
            </Select.Popup>
          </Select.Positioner>
        </Select.Portal>
      </Select.Root>
    </div>
  )
}