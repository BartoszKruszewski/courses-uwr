import Section from './Section'
import SkillList from './SkillList'

interface SkillsSectionProps {
  skills: string[]
}

function SkillsSection({ skills }: SkillsSectionProps) {
  return (
    <Section title="Umiejętności">
      <SkillList skills={skills} />
    </Section>
  )
}

export default SkillsSection
