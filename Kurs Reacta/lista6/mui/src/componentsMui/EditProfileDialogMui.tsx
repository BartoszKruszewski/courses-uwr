import {
  Autocomplete,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Stack,
  TextField,
} from '@mui/material'
import { useMemo } from 'react'
import type { Skill, SkillCategory } from '../model'

type EditableProfile = {
  name: string
  bio: string
  skills: Skill[]
}

type SkillOption = {
  name: string
  category: SkillCategory
}

type EditProfileDialogMuiProps = {
  open: boolean
  data: EditableProfile
  allSkillOptions: SkillOption[]
  onDataChange: (updated: EditableProfile) => void
  onClose: () => void
  onSave: () => void
}

function EditProfileDialogMui({
  open,
  data,
  allSkillOptions,
  onDataChange,
  onClose,
  onSave,
}: EditProfileDialogMuiProps) {
  const normalizedSkillOptions = useMemo(
    () =>
      allSkillOptions.map((option) => ({
        name: option.name,
        category: option.category,
      })),
    [allSkillOptions],
  )

  const handleNameChange = (name: string) => onDataChange({ ...data, name })
  const handleBioChange = (bio: string) => onDataChange({ ...data, bio })
  const handleSkillsChange = (skills: SkillOption[]) => onDataChange({ ...data, skills })

  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="sm">
      <DialogTitle>Edit profile</DialogTitle>
      <DialogContent>
        <Stack spacing={2} sx={{ pt: 1 }}>
          <TextField
            label="Name and surname"
            value={data.name}
            onChange={(e) => handleNameChange(e.target.value)}
            fullWidth
          />
          <TextField
            label="Description"
            value={data.bio}
            onChange={(e) => handleBioChange(e.target.value)}
            fullWidth
            multiline
            minRows={4}
          />
          <Autocomplete
            multiple
            options={normalizedSkillOptions}
            value={data.skills}
            onChange={(_, value) => handleSkillsChange(value)}
            disableCloseOnSelect
            getOptionLabel={(option) => option.name}
            isOptionEqualToValue={(option, value) => option.name === value.name}
            renderInput={(params) => <TextField {...params} label="Skills" placeholder="Select skills" />}
          />
        </Stack>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button onClick={onSave} variant="contained">
          Save
        </Button>
      </DialogActions>
    </Dialog>
  )
}

export type { EditableProfile, SkillOption }
export default EditProfileDialogMui
