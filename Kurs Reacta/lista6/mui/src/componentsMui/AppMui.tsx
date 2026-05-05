import { Box, Container, CssBaseline, ThemeProvider } from '@mui/material'
import { useMemo, useState } from 'react'
import { type Skill, type ThemeMode } from '../model'
import { experience, profile, skills as initialSkills } from '../profileData'
import AboutCardMui from './AboutCardMui'
import ContactCardMui from './ContactCardMui'
import EditProfileDialogMui, { type EditableProfile, type SkillOption } from './EditProfileDialogMui'
import ExperienceCardMui from './ExperienceCardMui'
import ProfileCardMui from './ProfileCardMui'
import SkillsCardMui from './SkillsCardMui'
import { themesMap } from './theme'
import TopBarMui from './TopBarMui'

function AppMui() {
  const [theme, setTheme] = useState<ThemeMode>('light')
  const [dialogOpen, setDialogOpen] = useState(false)
  const [editable, setEditable] = useState<EditableProfile>({
    name: profile.name,
    bio: profile.bio,
    skills: initialSkills,
  })
  const [draft, setDraft] = useState<EditableProfile>(editable)

  const allSkillOptions = useMemo<SkillOption[]>(
    () =>
      initialSkills.map((skill) => ({
        name: skill.name,
        category: skill.category,
      })),
    [],
  )

  const activeTheme = themesMap[theme]

  const openEditDialog = () => {
    setDraft(editable)
    setDialogOpen(true)
  }

  const handleSave = () => {
    const fallbackName = draft.name.trim() || profile.name
    const fallbackBio = draft.bio.trim() || profile.bio

    setEditable({
      name: fallbackName,
      bio: fallbackBio,
      skills: normalizeSkillCategories(draft.skills, allSkillOptions),
    })
    setDialogOpen(false)
  }

  return (
    <ThemeProvider theme={activeTheme}>
      <CssBaseline />
      <Box sx={{ minHeight: '100vh', py: 4, px: 2, bgcolor: 'background.default' }}>
        <Container maxWidth="md" sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <TopBarMui theme={theme} onThemeChange={setTheme} />
          <ProfileCardMui
            name={editable.name}
            title={profile.title}
            location={profile.location}
            avatar={profile.avatar}
            onEdit={openEditDialog}
          />
          <AboutCardMui text={editable.bio} />
          <SkillsCardMui skills={editable.skills} />
          <ExperienceCardMui experience={experience} />
          <ContactCardMui email={profile.email} github={profile.github} linkedin={profile.linkedin} />
        </Container>
      </Box>

      <EditProfileDialogMui
        open={dialogOpen}
        data={draft}
        allSkillOptions={allSkillOptions}
        onDataChange={setDraft}
        onClose={() => setDialogOpen(false)}
        onSave={handleSave}
      />
    </ThemeProvider>
  )
}

function normalizeSkillCategories(skills: Skill[], options: SkillOption[]): Skill[] {
  const categoryByName = new Map(options.map((option) => [option.name, option.category]))

  return skills.map((skill) => ({
    name: skill.name,
    category: categoryByName.get(skill.name) ?? skill.category,
  }))
}

export default AppMui
