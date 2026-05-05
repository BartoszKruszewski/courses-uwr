import { type ReactNode } from 'react'
import { Accordion } from '@base-ui/react'

export interface SettingsAccordionProps {
  children: ReactNode
  defaultValue?: string[]
}

export function SettingsAccordion({
  children,
  defaultValue = ['profile', 'notifications', 'appearance'],
}: SettingsAccordionProps) {
  return (
    <Accordion.Root
      multiple
      keepMounted
      defaultValue={defaultValue}
      className="settings-accordion"
    >
      {children}
    </Accordion.Root>
  )
}