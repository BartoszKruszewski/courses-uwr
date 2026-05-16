import type { Dispatch, SetStateAction } from 'react'
import { Slider } from '@base-ui/react'
import { SettingsTooltip } from './SettingsTooltip'

export interface SettingsSliderProps {
  description?: string
  formatValue?: (value: number) => string
  label: string
  max?: number
  min?: number
  onValueChange: Dispatch<SetStateAction<number>>
  step?: number
  tooltip?: string
  value: number
}

export function SettingsSlider({
  description,
  formatValue = (value) => `${value}`,
  label,
  max = 24,
  min = 12,
  onValueChange,
  step = 1,
  tooltip,
  value,
}: SettingsSliderProps) {
  return (
    <div className="settings-slider-shell">
      <div className="settings-field-heading settings-slider-heading">
        <div className="settings-slider-title-row">
          <span className="settings-field-label">{label}</span>
          {tooltip ? (
            <SettingsTooltip content={tooltip} label={tooltip}>
              <span aria-hidden="true">i</span>
            </SettingsTooltip>
          ) : null}
        </div>
        {description ? <span className="settings-field-description">{description}</span> : null}
      </div>

      <div className="settings-slider-value">{formatValue(value)}</div>

      <Slider.Root
        className="settings-slider-root"
        value={value}
        min={min}
        max={max}
        step={step}
        onValueChange={onValueChange}
      >
        <Slider.Control className="settings-slider-control">
          <Slider.Track className="settings-slider-track">
            <Slider.Indicator className="settings-slider-indicator" />
          </Slider.Track>
          <Slider.Thumb className="settings-slider-thumb" />
        </Slider.Control>
      </Slider.Root>
    </div>
  )
}