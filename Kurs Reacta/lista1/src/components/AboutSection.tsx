import Section from './Section'
import './AboutSection.css'

interface AboutSectionProps {
  text: string
}

function AboutSection({ text }: AboutSectionProps) {
  return (
    <Section title="O mnie">
      <p className="about-section__text">{text}</p>
    </Section>
  )
}

export default AboutSection
