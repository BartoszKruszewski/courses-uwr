import { useState } from 'react'
import type { ThemeMode } from '../model'
import { experience, profile, skills } from '../profileData'
import AboutCard from './AboutCard'
import ContactCard from './ContactCard'
import ExperienceCard from './ExperienceCard'
import ProfileCard from './ProfileCard'
import SkillsCard from './SkillsCard'
import './tailwind.css'
import TopBar from './TopBar'

function AppTailwind() {
  const [theme, setTheme] = useState<ThemeMode>('light')

  return (
    <div
      className={`theme-${theme} min-h-screen px-4 py-8 text-slate-700 transition-colors light:bg-slate-100 dark:bg-slate-900 dark:text-slate-300 midnight:bg-[#1a1025] midnight:text-violet-300`}
    >
      <div className="mx-auto flex max-w-3xl flex-col gap-4">
        <TopBar theme={theme} onThemeChange={setTheme} />
        <ProfileCard
          name={profile.name}
          title={profile.title}
          location={profile.location}
          avatar={profile.avatar}
        />
        <AboutCard text={profile.bio} />
        <SkillsCard skills={skills} />
        <ExperienceCard experience={experience} />
        <ContactCard
          email={profile.email}
          github={profile.github}
          linkedin={profile.linkedin}
        />
      </div>
    </div>
  )
}

export default AppTailwind
