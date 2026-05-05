import { Box, Card, CardContent, Chip, Stack, Typography } from '@mui/material'
import { skillCategories, type Skill, type SkillCategory } from '../model'

const categoryLabels: Record<SkillCategory, string> = {
  language: 'Languages',
  framework: 'Frameworks',
  tool: 'Tools',
  soft: 'Soft Skills',
}

const chipStyles: Record<SkillCategory, object> = {
  language: {
    bgcolor: '#dbeafe',
    color: '#1e40af',
    borderColor: '#93c5fd',
  },
  framework: {
    bgcolor: '#dcfce7',
    color: '#166534',
    borderColor: '#86efac',
  },
  tool: {
    bgcolor: '#fef3c7',
    color: '#92400e',
    borderColor: '#fcd34d',
  },
  soft: {
    bgcolor: '#ede9fe',
    color: '#5b21b6',
    borderColor: '#c4b5fd',
  },
}

type SkillsCardMuiProps = {
  skills: Skill[]
}

function SkillsCardMui({ skills }: SkillsCardMuiProps) {
  const grouped = skillCategories
    .map((category) => ({
      category,
      label: categoryLabels[category],
      items: skills.filter((skill) => skill.category === category),
    }))
    .filter((group) => group.items.length > 0)

  return (
    <Card>
      <CardContent>
        <Typography variant="overline" color="text.secondary">
          Skills
        </Typography>

        <Stack spacing={1.5}>
          {grouped.map((group) => (
            <Box key={group.category}>
              <Typography variant="caption" sx={{ display: 'block', mb: 0.75, textTransform: 'uppercase' }}>
                {group.label}
              </Typography>
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.75 }}>
                {group.items.map((skill) => (
                  <Chip
                    key={skill.name}
                    label={skill.name}
                    sx={{
                      fontWeight: 500,
                      ...chipStyles[skill.category],
                    }}
                  />
                ))}
              </Box>
            </Box>
          ))}
        </Stack>
      </CardContent>
    </Card>
  )
}

export default SkillsCardMui
