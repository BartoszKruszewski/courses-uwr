import { useState } from 'react'
import type { Experience, Skill, SkillCategory, ThemeMode } from '../model'
import { skillCategories, themes } from '../model'
import { experience, profile, skills } from '../profileData'
import styles from './AppScss.module.scss'

const categoryLabels: Record<SkillCategory, string> = {
  language: 'Languages',
  framework: 'Frameworks',
  tool: 'Tools',
  soft: 'Soft Skills',
}

const chipClassByCategory: Record<SkillCategory, string> = {
  language: styles.chipLanguage,
  framework: styles.chipFramework,
  tool: styles.chipTool,
  soft: styles.chipSoft,
}

function TopBar({
  theme,
  onThemeChange,
}: {
  theme: ThemeMode
  onThemeChange: (t: ThemeMode) => void
}) {
  return (
    <div className={`${styles.card} ${styles.topBar}`}>
      <h1 className={styles.appTitle}>Theme Showcase</h1>
      <select
        className={styles.themeSelect}
        value={theme}
        onChange={(e) => onThemeChange(e.target.value as ThemeMode)}
      >
        {themes.map((t) => (
          <option key={t} value={t}>
            {t.charAt(0).toUpperCase() + t.slice(1)}
          </option>
        ))}
      </select>
    </div>
  )
}

function ProfileCard({
  name,
  title,
  location,
  avatar,
}: {
  name: string
  title: string
  location: string
  avatar: string
}) {
  return (
    <div className={`${styles.card} ${styles.profileCard}`}>
      <div className={styles.profileAvatar}>{avatar}</div>
      <div>
        <h2 className={styles.profileName}>{name}</h2>
        <p className={styles.profileTitle}>{title}</p>
        <p className={styles.profileLocation}>{location}</p>
      </div>
    </div>
  )
}

function AboutCard({ text }: { text: string }) {
  return (
    <div className={styles.card}>
      <h3 className={styles.cardHeading}>About</h3>
      <p className={styles.aboutText}>{text}</p>
    </div>
  )
}

function SkillsCard({ skillsList }: { skillsList: Skill[] }) {
  const grouped = skillCategories
    .map((cat) => ({
      category: cat,
      label: categoryLabels[cat],
      items: skillsList.filter((s) => s.category === cat),
    }))
    .filter((g) => g.items.length > 0)

  return (
    <div className={styles.card}>
      <h3 className={styles.cardHeading}>Skills</h3>
      {grouped.map((group) => (
        <div key={group.category} className={styles.skillGroup}>
          <p className={styles.skillGroupLabel}>{group.label}</p>
          <div className={styles.skillChips}>
            {group.items.map((s) => (
              <span
                key={s.name}
                className={`${styles.chip} ${chipClassByCategory[s.category]}`}
              >
                {s.name}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}

function ExperienceCard({ experienceList }: { experienceList: Experience[] }) {
  return (
    <div className={styles.card}>
      <h3 className={styles.cardHeading}>Experience</h3>
      <div className={styles.experienceList}>
        {experienceList.map((exp) => (
          <div key={exp.company} className={styles.experienceItem}>
            <div>
              <p className={styles.experienceRole}>{exp.role}</p>
              <p className={styles.experienceCompany}>{exp.company}</p>
            </div>
            <span className={styles.experiencePeriod}>{exp.period}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

function ContactCard({
  email,
  github,
  linkedin,
}: {
  email: string
  github: string
  linkedin: string
}) {
  return (
    <div className={styles.card}>
      <h3 className={styles.cardHeading}>Contact</h3>
      <div className={styles.contactList}>
        <p className={styles.contactItem}>
          <span className={styles.contactLabel}>Email</span>
          {email}
        </p>
        <p className={styles.contactItem}>
          <span className={styles.contactLabel}>GitHub</span>
          {github}
        </p>
        <p className={styles.contactItem}>
          <span className={styles.contactLabel}>LinkedIn</span>
          {linkedin}
        </p>
      </div>
    </div>
  )
}

function AppScss() {
  const [theme, setTheme] = useState<ThemeMode>('light')

  return (
    <div className={`theme-${theme}`}>
      <div className={styles.app}>
        <div className={styles.container}>
          <TopBar theme={theme} onThemeChange={setTheme} />
          <ProfileCard
            name={profile.name}
            title={profile.title}
            location={profile.location}
            avatar={profile.avatar}
          />
          <AboutCard text={profile.bio} />
          <SkillsCard skillsList={skills} />
          <ExperienceCard experienceList={experience} />
          <ContactCard
            email={profile.email}
            github={profile.github}
            linkedin={profile.linkedin}
          />
        </div>
      </div>
    </div>
  )
}

export default AppScss
