import { Card, CardContent, MenuItem, Select, Stack, Typography } from '@mui/material'
import { themes, type ThemeMode } from '../model'

type TopBarMuiProps = {
  theme: ThemeMode
  onThemeChange: (theme: ThemeMode) => void
}

function TopBarMui({ theme, onThemeChange }: TopBarMuiProps) {
  return (
    <Card>
      <CardContent>
        <Stack direction="row" spacing={2} sx={{ alignItems: 'center', justifyContent: 'space-between' }}>
          <Typography variant="h6">
          Theme Showcase
          </Typography>
          <Select
            size="small"
            value={theme}
            onChange={(e) => onThemeChange(e.target.value as ThemeMode)}
            sx={{ minWidth: 132, textTransform: 'capitalize' }}
          >
            {themes.map((item) => (
              <MenuItem key={item} value={item} sx={{ textTransform: 'capitalize' }}>
                {item}
              </MenuItem>
            ))}
          </Select>
        </Stack>
      </CardContent>
    </Card>
  )
}

export default TopBarMui
