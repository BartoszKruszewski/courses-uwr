import { Card, CardContent, List, ListItem, Stack, Typography } from '@mui/material'
import type { Experience } from '../model'

type ExperienceCardMuiProps = {
  experience: Experience[]
}

function ExperienceCardMui({ experience }: ExperienceCardMuiProps) {
  return (
    <Card>
      <CardContent>
        <Typography variant="overline" color="text.secondary">
          Experience
        </Typography>

        <List disablePadding>
          {experience.map((exp) => (
            <ListItem key={`${exp.company}-${exp.role}`} disableGutters sx={{ py: 1 }}>
              <Stack direction="row" spacing={2} sx={{ justifyContent: 'space-between', alignItems: 'baseline', width: '100%' }}>
                <Stack spacing={0.25}>
                  <Typography variant="body2" sx={{ fontWeight: 600 }}>
                    {exp.role}
                  </Typography>
                  <Typography variant="caption" color="text.secondary">
                    {exp.company}
                  </Typography>
                </Stack>
                <Typography variant="caption" color="text.secondary" sx={{ whiteSpace: 'nowrap' }}>
                  {exp.period}
                </Typography>
              </Stack>
            </ListItem>
          ))}
        </List>
      </CardContent>
    </Card>
  )
}

export default ExperienceCardMui
