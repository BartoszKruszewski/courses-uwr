import { Card, CardContent, List, ListItem, Stack, Typography } from '@mui/material'

type ContactCardMuiProps = {
  email: string
  github: string
  linkedin: string
}

function ContactCardMui({ email, github, linkedin }: ContactCardMuiProps) {
  const contacts = [
    { label: 'Email', value: email },
    { label: 'GitHub', value: github },
    { label: 'LinkedIn', value: linkedin },
  ]

  return (
    <Card>
      <CardContent>
        <Typography variant="overline" color="text.secondary">
          Contact
        </Typography>

        <List disablePadding>
          {contacts.map((item) => (
            <ListItem key={item.label} disableGutters sx={{ py: 0.5 }}>
              <Stack direction="row" spacing={1}>
                <Typography variant="body2" sx={{ fontWeight: 600 }}>
                  {item.label}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  {item.value}
                </Typography>
              </Stack>
            </ListItem>
          ))}
        </List>
      </CardContent>
    </Card>
  )
}

export default ContactCardMui
