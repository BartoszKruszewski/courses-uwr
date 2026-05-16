import { type ReactNode } from 'react'
import { Tooltip } from '@base-ui/react'

export interface SettingsTooltipProps {
  children?: ReactNode
  content: ReactNode
  label: string
}

export function SettingsTooltip({ children, content, label }: SettingsTooltipProps) {
  return (
    <Tooltip.Root>
      <Tooltip.Trigger className="settings-tooltip-trigger" aria-label={label}>
        {children ?? <span aria-hidden="true">i</span>}
      </Tooltip.Trigger>
      <Tooltip.Portal>
        <Tooltip.Positioner className="settings-tooltip-positioner" sideOffset={10}>
          <Tooltip.Popup className="settings-tooltip-popup">
            <Tooltip.Arrow className="settings-tooltip-arrow" />
            <Tooltip.Viewport className="settings-tooltip-viewport">{content}</Tooltip.Viewport>
          </Tooltip.Popup>
        </Tooltip.Positioner>
      </Tooltip.Portal>
    </Tooltip.Root>
  )
}