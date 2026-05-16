import { Avatar, Button, Card, CardContent, Stack, Typography } from '@mui/material'

type ProfileCardMuiProps = {
  name: string
  title: string
  location: string
  avatar: string
  onEdit: () => void
}

function ProfileCardMui({ name, title, location, avatar, onEdit }: ProfileCardMuiProps) {
  return (
    <Card>
      <CardContent>
        <Stack direction="row" spacing={2} sx={{ alignItems: 'center', justifyContent: 'space-between' }}>
          <Stack direction="row" spacing={2.5} sx={{ alignItems: 'center' }}>
            <Avatar sx={{ width: 72, height: 72, fontWeight: 700, bgcolor: 'primary.main' }}>
              {avatar}
            </Avatar>
            <div>
              <Typography variant="h5" sx={{ fontWeight: 700 }}>
              {name}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {title}
              </Typography>
              <Typography variant="caption" color="text.secondary">
                {location}
              </Typography>
            </div>
          </Stack>
          <Button variant="contained" onClick={onEdit}>
            Edit
          </Button>
        </Stack>
      </CardContent>
    </Card>
  )
}

export default ProfileCardMui
