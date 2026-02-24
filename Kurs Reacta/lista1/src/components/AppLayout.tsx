import type { ReactNode } from 'react'
import './AppLayout.css'

interface AppLayoutProps {
  children: ReactNode
}

function AppLayout({ children }: AppLayoutProps) {
  return (
    <div className="app-layout">
      <main className="app-layout__content">{children}</main>
    </div>
  )
}

export default AppLayout
