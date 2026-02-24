import './SkillItem.css'

interface SkillItemProps {
  label: string
}

function SkillItem({ label }: SkillItemProps) {
  return <li className="skill-item">{label}</li>
}

export default SkillItem
