import { Global, ThemeProvider, css } from '@emotion/react'
import styled from '@emotion/styled'
import { useState } from 'react'
import { experience, profile, skills } from '../profileData'
import {
  skillCategories,
  themes,
  type Skill,
  type SkillCategory,
  type ThemeMode,
} from '../model'
import type { AppTheme } from './theme'
import { appThemes } from './theme'

const categoryLabels: Record<SkillCategory, string> = {
  language: 'Languages',
  framework: 'Frameworks',
  tool: 'Tools',
  soft: 'Soft Skills',
}

const globalStyles = (theme: AppTheme) => css`
  * {
    box-sizing: border-box;
  }

  body {
    margin: 0;
    font-family: "Inter", "Segoe UI", sans-serif;
    background: ${theme.colors.pageBackground};
    color: ${theme.colors.bodyText};
  }

  #root {
    min-height: 100vh;
  }
`

const AppShell = styled.div`
  min-height: 100vh;
  padding: 32px 16px;
  background: ${({ theme }) => theme.colors.pageBackground};
  color: ${({ theme }) => theme.colors.bodyText};
`

const Container = styled.div`
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
`

const Card = styled.div`
  border-radius: 12px;
  padding: 24px;
  border: 1px solid ${({ theme }) => theme.colors.surfaceBorder};
  background: ${({ theme }) => theme.colors.surfaceBackground};
`

const TopBarCard = styled(Card)`
  display: flex;
  align-items: center;
  justify-content: space-between;
`

const AppTitle = styled.h1`
  margin: 0;
  font-size: 1rem;
  font-weight: 700;
  color: ${({ theme }) => theme.colors.strongText};
`

const ThemeSelect = styled.select`
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid ${({ theme }) => theme.colors.controlBorder};
  background: ${({ theme }) => theme.colors.controlBackground};
  color: ${({ theme }) => theme.colors.controlText};
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
`

const ProfileCardFrame = styled(Card)`
  display: flex;
  align-items: center;
  gap: 20px;
`

const ProfileAvatar = styled.div`
  width: 72px;
  height: 72px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  font-weight: 700;
  color: #ffffff;
  flex-shrink: 0;
  background: ${({ theme }) => theme.colors.avatarBackground};
`

const ProfileName = styled.h2`
  margin: 0;
  font-size: 1.3rem;
  font-weight: 700;
  color: ${({ theme }) => theme.colors.strongText};
`

const ProfileTitle = styled.p`
  margin: 4px 0 0;
  font-size: 0.9rem;
  font-weight: 500;
  opacity: 0.75;
`

const ProfileLocation = styled.p`
  margin: 4px 0 0;
  font-size: 0.8rem;
  opacity: 0.6;
`

const CardHeading = styled.h3`
  margin: 0 0 10px;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: ${({ theme }) => theme.colors.headingText};
`

const AboutText = styled.p`
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.65;
`

const SkillGroup = styled.div`
  margin-bottom: 12px;

  &:last-child {
    margin-bottom: 0;
  }
`

const SkillGroupLabel = styled.p`
  margin: 0 0 6px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  opacity: 0.6;
`

const SkillChips = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
`

const Chip = styled('span', {
  shouldForwardProp: (prop) => prop !== 'category',
})<{ category: SkillCategory }>`
  padding: 4px 12px;
  border-radius: 999px;
  font-size: 0.78rem;
  font-weight: 500;
  border: 1px solid;
  background: ${({ theme, category }) => theme.chips[category].background};
  color: ${({ theme, category }) => theme.chips[category].text};
  border-color: ${({ theme, category }) => theme.chips[category].border};
`

const ExperienceList = styled.div`
  display: flex;
  flex-direction: column;
  gap: 12px;
`

const ExperienceItem = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 12px;
`

const ExperienceRole = styled.p`
  margin: 0;
  font-weight: 600;
  font-size: 0.9rem;
  color: ${({ theme }) => theme.colors.strongText};
`

const ExperienceCompany = styled.p`
  margin: 2px 0 0;
  font-size: 0.8rem;
  opacity: 0.65;
`

const ExperiencePeriod = styled.span`
  font-size: 0.78rem;
  white-space: nowrap;
  opacity: 0.55;
`

const ContactList = styled.div`
  display: flex;
  flex-direction: column;
  gap: 6px;
`

const ContactItem = styled.p`
  margin: 0;
  font-size: 0.88rem;
`

const ContactLabel = styled.span`
  font-weight: 600;
  margin-right: 6px;
  color: ${({ theme }) => theme.colors.contactLabelText};
`

function AppCssInJs() {
  const [themeMode, setThemeMode] = useState<ThemeMode>('light')
  const theme = appThemes[themeMode]

  const groupedSkills = skillCategories
    .map((category) => ({
      category,
      label: categoryLabels[category],
      items: skills.filter((skill) => skill.category === category),
    }))
    .filter((group) => group.items.length > 0)

  return (
    <ThemeProvider theme={theme}>
      <>
        <Global styles={globalStyles(theme)} />
        <AppShell>
          <Container>
            <TopBarCard>
              <AppTitle>Theme Showcase</AppTitle>
              <ThemeSelect
                value={themeMode}
                onChange={(event) => setThemeMode(event.target.value as ThemeMode)}
              >
                {themes.map((mode) => (
                  <option key={mode} value={mode}>
                    {mode.charAt(0).toUpperCase() + mode.slice(1)}
                  </option>
                ))}
              </ThemeSelect>
            </TopBarCard>

            <ProfileCardFrame>
              <ProfileAvatar>{profile.avatar}</ProfileAvatar>
              <div>
                <ProfileName>{profile.name}</ProfileName>
                <ProfileTitle>{profile.title}</ProfileTitle>
                <ProfileLocation>{profile.location}</ProfileLocation>
              </div>
            </ProfileCardFrame>

            <Card>
              <CardHeading>About</CardHeading>
              <AboutText>{profile.bio}</AboutText>
            </Card>

            <Card>
              <CardHeading>Skills</CardHeading>
              {groupedSkills.map((group) => (
                <SkillGroup key={group.category}>
                  <SkillGroupLabel>{group.label}</SkillGroupLabel>
                  <SkillChips>
                    {group.items.map((skill: Skill) => (
                      <Chip key={skill.name} category={skill.category}>
                        {skill.name}
                      </Chip>
                    ))}
                  </SkillChips>
                </SkillGroup>
              ))}
            </Card>

            <Card>
              <CardHeading>Experience</CardHeading>
              <ExperienceList>
                {experience.map((item) => (
                  <ExperienceItem key={item.company}>
                    <div>
                      <ExperienceRole>{item.role}</ExperienceRole>
                      <ExperienceCompany>{item.company}</ExperienceCompany>
                    </div>
                    <ExperiencePeriod>{item.period}</ExperiencePeriod>
                  </ExperienceItem>
                ))}
              </ExperienceList>
            </Card>

            <Card>
              <CardHeading>Contact</CardHeading>
              <ContactList>
                <ContactItem>
                  <ContactLabel>Email</ContactLabel>
                  {profile.email}
                </ContactItem>
                <ContactItem>
                  <ContactLabel>GitHub</ContactLabel>
                  {profile.github}
                </ContactItem>
                <ContactItem>
                  <ContactLabel>LinkedIn</ContactLabel>
                  {profile.linkedin}
                </ContactItem>
              </ContactList>
            </Card>
          </Container>
        </AppShell>
      </>
    </ThemeProvider>
  )
}

export default AppCssInJs
