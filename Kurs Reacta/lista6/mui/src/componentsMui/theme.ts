import { createTheme, type Theme } from '@mui/material/styles'
import type { ThemeMode } from '../model'

const sharedShape = {
  borderRadius: 3,
}

const baseTypography = {
  fontFamily: '"Inter", "Segoe UI", sans-serif',
}

const sharedComponents = {
  MuiCard: {
    defaultProps: {
      variant: 'outlined' as const,
    },
    styleOverrides: {
      root: {
        borderRadius: 12,
      },
    },
  },
  MuiCardContent: {
    styleOverrides: {
      root: {
        padding: 24,
        '&:last-child': {
          paddingBottom: 24,
        },
      },
    },
  },
  MuiButton: {
    defaultProps: {
      disableElevation: true,
    },
  },
  MuiChip: {
    defaultProps: {
      size: 'small' as const,
      variant: 'outlined' as const,
    },
  },
}

export const themesMap: Record<ThemeMode, Theme> = {
  light: createTheme({
    palette: {
      mode: 'light',
      background: {
        default: '#f1f5f9',
        paper: '#ffffff',
      },
      text: {
        primary: '#0f172a',
        secondary: '#475569',
      },
      divider: '#e2e8f0',
      primary: {
        main: '#2563eb',
      },
    },
    shape: sharedShape,
    typography: baseTypography,
    components: sharedComponents,
  }),
  dark: createTheme({
    palette: {
      mode: 'dark',
      background: {
        default: '#0f172a',
        paper: '#1e293b',
      },
      text: {
        primary: '#f1f5f9',
        secondary: '#94a3b8',
      },
      divider: '#334155',
      primary: {
        main: '#6366f1',
      },
    },
    shape: sharedShape,
    typography: baseTypography,
    components: sharedComponents,
  }),
  midnight: createTheme({
    palette: {
      mode: 'dark',
      background: {
        default: '#1a1025',
        paper: '#261838',
      },
      text: {
        primary: '#e9d5ff',
        secondary: '#c4b5fd',
      },
      divider: '#3b2756',
      primary: {
        main: '#7c3aed',
      },
    },
    shape: sharedShape,
    typography: baseTypography,
    components: sharedComponents,
  }),
}
