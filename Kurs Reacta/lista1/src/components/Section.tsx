import type { ReactNode } from 'react'
import './Section.css'

interface SectionProps {
  title: string
  children: ReactNode
}

function Section({ title, children }: SectionProps) {
  return (
    <section className="section">
      <h2 className="section__title">{title}</h2>
      <div className="section__content">{children}</div>
    </section>
  )
}

export default Section
