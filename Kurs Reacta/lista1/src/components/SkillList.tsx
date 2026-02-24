import SkillItem from './SkillItem'
import './SkillList.css'

interface SkillListProps {
  skills: string[]
}

function SkillList({ skills }: SkillListProps) {
  return (
    <ul className="skill-list">
      {skills.map((skill) => (
        <SkillItem key={skill} label={skill} />
      ))}
    </ul>
  )
}

export default SkillList
