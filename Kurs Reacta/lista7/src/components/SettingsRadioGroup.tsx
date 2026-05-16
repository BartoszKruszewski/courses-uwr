import type { Dispatch, SetStateAction } from 'react'
import { Radio, RadioGroup } from '@base-ui/react'

export interface RadioOption<Value extends string = string> {
  description?: string
  label: string
  value: Value
}

export interface SettingsRadioGroupProps<Value extends string = string> {
  description?: string
  label: string
  onValueChange: Dispatch<SetStateAction<Value>>
  options: readonly RadioOption<Value>[]
  value: Value
}

export function SettingsRadioGroup<Value extends string = string>({
  description,
  label,
  onValueChange,
  options,
  value,
}: SettingsRadioGroupProps<Value>) {
  return (
    <section className="settings-radio-group-shell">
      <div className="settings-group-heading">
        <h3>{label}</h3>
        {description ? <p>{description}</p> : null}
      </div>

      <RadioGroup
        className="settings-radio-group"
        value={value}
        onValueChange={onValueChange}
      >
        {options.map((option) => (
          <label key={option.value} className="settings-radio-option">
            <Radio.Root value={option.value} className="settings-radio-root">
              <Radio.Indicator className="settings-radio-indicator" />
            </Radio.Root>

            <span className="settings-radio-copy">
              <span className="settings-radio-label">{option.label}</span>
              {option.description ? (
                <span className="settings-radio-description">{option.description}</span>
              ) : null}
            </span>
          </label>
        ))}
      </RadioGroup>
    </section>
  )
}