import { Card, CardContent, Typography } from '@mui/material'

type AboutCardMuiProps = {
  text: string
}

function AboutCardMui({ text }: AboutCardMuiProps) {
  return (
    <Card>
      <CardContent>
        <Typography variant="overline" color="text.secondary">
          About
        </Typography>
        <Typography variant="body2" sx={{ lineHeight: 1.7 }}>
          {text}
        </Typography>
      </CardContent>
    </Card>
  )
}

export default AboutCardMui
