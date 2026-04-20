import type { SkillCategory, ThemeMode } from '../model'

export type AppTheme = {
  mode: ThemeMode
  colors: {
    pageBackground: string
    bodyText: string
    surfaceBackground: string
    surfaceBorder: string
    strongText: string
    headingText: string
    controlBackground: string
    controlBorder: string
    controlText: string
    avatarBackground: string
    contactLabelText: string
  }
  chips: Record<SkillCategory, {
    background: string
    text: string
    border: string
  }>
}

const chipTokens: AppTheme['chips'] = {
  language: {
    background: '#dbeafe',
    text: '#1e40af',
    border: '#93c5fd',
  },
  framework: {
    background: '#dcfce7',
    text: '#166534',
    border: '#86efac',
  },
  tool: {
    background: '#fef3c7',
    text: '#92400e',
    border: '#fcd34d',
  },
  soft: {
    background: '#ede9fe',
    text: '#5b21b6',
    border: '#c4b5fd',
  },
}

export const appThemes: Record<ThemeMode, AppTheme> = {
  light: {
    mode: 'light',
    colors: {
      pageBackground: '#f1f5f9',
      bodyText: '#334155',
      surfaceBackground: '#ffffff',
      surfaceBorder: '#e2e8f0',
      strongText: '#0f172a',
      headingText: '#64748b',
      controlBackground: '#f8fafc',
      controlBorder: '#cbd5e1',
      controlText: '#334155',
      avatarBackground: '#3b82f6',
      contactLabelText: '#0f172a',
    },
    chips: chipTokens,
  },
  dark: {
    mode: 'dark',
    colors: {
      pageBackground: '#0f172a',
      bodyText: '#94a3b8',
      surfaceBackground: '#1e293b',
      surfaceBorder: '#334155',
      strongText: '#f1f5f9',
      headingText: '#64748b',
      controlBackground: '#0f172a',
      controlBorder: '#475569',
      controlText: '#e2e8f0',
      avatarBackground: '#6366f1',
      contactLabelText: '#e2e8f0',
    },
    chips: chipTokens,
  },
  midnight: {
    mode: 'midnight',
    colors: {
      pageBackground: '#1a1025',
      bodyText: '#c4b5fd',
      surfaceBackground: '#261838',
      surfaceBorder: '#3b2756',
      strongText: '#e9d5ff',
      headingText: '#8b5cf6',
      controlBackground: '#1a1025',
      controlBorder: '#5b21b6',
      controlText: '#e9d5ff',
      avatarBackground: '#7c3aed',
      contactLabelText: '#c4b5fd',
    },
    chips: chipTokens,
  },
}