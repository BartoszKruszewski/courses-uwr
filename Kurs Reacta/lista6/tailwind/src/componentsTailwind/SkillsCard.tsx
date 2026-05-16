import { skillCategories, type Skill, type SkillCategory } from '../model'

const categoryLabels: Record<SkillCategory, string> = {
  language: 'Languages',
  framework: 'Frameworks',
  tool: 'Tools',
  soft: 'Soft Skills',
}

const chipStyles: Record<SkillCategory, string> = {
  language: 'bg-blue-100 text-blue-800 border-blue-300 dark:bg-blue-900/50 dark:text-blue-200 dark:border-blue-700 midnight:bg-blue-950/50 midnight:text-blue-200 midnight:border-blue-700',
  framework:
    'bg-emerald-100 text-emerald-800 border-emerald-300 dark:bg-emerald-900/45 dark:text-emerald-200 dark:border-emerald-700 midnight:bg-emerald-950/45 midnight:text-emerald-200 midnight:border-emerald-700',
  tool: 'bg-amber-100 text-amber-800 border-amber-300 dark:bg-amber-900/45 dark:text-amber-200 dark:border-amber-700 midnight:bg-amber-950/40 midnight:text-amber-200 midnight:border-amber-700',
  soft: 'bg-violet-100 text-violet-800 border-violet-300 dark:bg-violet-900/45 dark:text-violet-200 dark:border-violet-700 midnight:bg-violet-950/45 midnight:text-violet-200 midnight:border-violet-600',
}

function SkillsCard({ skills }: { skills: Skill[] }) {
  const grouped = skillCategories
    .map((cat) => ({
      category: cat,
      label: categoryLabels[cat],
      items: skills.filter((s) => s.category === cat),
    }))
    .filter((g) => g.items.length > 0)

  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6 dark:border-slate-700 dark:bg-slate-800 midnight:border-[#3b2756] midnight:bg-[#261838]">
      <h3 className="m-0 mb-2.5 text-xs font-bold tracking-[0.1em] text-slate-500 uppercase dark:text-slate-500 midnight:text-violet-500">
        Skills
      </h3>
      {grouped.map((group) => (
        <div key={group.category} className="mb-3 last:mb-0">
          <p className="m-0 mb-1.5 text-xs font-semibold tracking-[0.06em] uppercase opacity-60">
            {group.label}
          </p>
          <div className="flex flex-wrap gap-1.5">
            {group.items.map((skill) => (
              <span
                key={skill.name}
                className={`rounded-full border px-3 py-1 text-[0.78rem] font-medium ${chipStyles[skill.category]}`}
              >
                {skill.name}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}

export default SkillsCard
