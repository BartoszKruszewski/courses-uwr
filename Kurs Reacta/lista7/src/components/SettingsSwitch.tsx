import type { Dispatch, SetStateAction } from 'react'
import { Switch } from '@base-ui/react'

export interface SettingsSwitchProps {
  checked: boolean
  description?: string
  label: string
  onCheckedChange: Dispatch<SetStateAction<boolean>>
}

export function SettingsSwitch({
  checked,
  description,
  label,
  onCheckedChange,
}: SettingsSwitchProps) {
  return (
    <label className="settings-switch">
      <span className="settings-switch-copy">
        <span className="settings-switch-label">{label}</span>
        {description ? <span className="settings-switch-description">{description}</span> : null}
      </span>

      <Switch.Root
        checked={checked}
        onCheckedChange={onCheckedChange}
        className="settings-switch-root"
      >
        <Switch.Thumb className="settings-switch-thumb" />
      </Switch.Root>
    </label>
  )
}