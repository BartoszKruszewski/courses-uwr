import type { Experience } from '../model'

function ExperienceCard({ experience }: { experience: Experience[] }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6 dark:border-slate-700 dark:bg-slate-800 midnight:border-[#3b2756] midnight:bg-[#261838]">
      <h3 className="m-0 mb-2.5 text-xs font-bold tracking-[0.1em] text-slate-500 uppercase dark:text-slate-500 midnight:text-violet-500">
        Experience
      </h3>
      <div className="flex flex-col gap-3">
        {experience.map((exp) => (
          <div key={exp.company} className="flex items-baseline justify-between gap-3">
            <div>
              <p className="m-0 text-[0.9rem] font-semibold text-slate-900 dark:text-slate-200 midnight:text-violet-100">
                {exp.role}
              </p>
              <p className="mt-0.5 mb-0 text-[0.8rem] opacity-65">{exp.company}</p>
            </div>
            <span className="text-[0.78rem] whitespace-nowrap opacity-55">{exp.period}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ExperienceCard
