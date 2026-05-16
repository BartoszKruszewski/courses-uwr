import { useMemo, useState } from 'react'
import { Accordion, Tooltip } from '@base-ui/react'
import './App.scss'
import {
  SettingsAccordion,
} from './components/SettingsAccordion'
import {
  SettingsCombobox,
  type ComboboxOption,
} from './components/SettingsCombobox'
import { SettingsConfirmationDialog } from './components/SettingsConfirmationDialog'
import {
  SettingsRadioGroup,
  type RadioOption,
} from './components/SettingsRadioGroup'
import { SettingsSelect, type SelectOption } from './components/SettingsSelect'
import { SettingsSlider } from './components/SettingsSlider'
import { SettingsSwitch } from './components/SettingsSwitch'

const skillOptions: ComboboxOption[] = [
  { value: 'accessibility', label: 'Accessibility' },
  { value: 'animations', label: 'Animations' },
  { value: 'css', label: 'CSS Architecture' },
  { value: 'design-systems', label: 'Design Systems' },
  { value: 'figma', label: 'Figma' },
  { value: 'frontend-architecture', label: 'Frontend Architecture' },
  { value: 'javascript', label: 'JavaScript' },
  { value: 'performance', label: 'Performance Tuning' },
  { value: 'react', label: 'React' },
  { value: 'testing', label: 'Testing' },
  { value: 'typescript', label: 'TypeScript' },
  { value: 'ux-writing', label: 'UX Writing' },
]

type LanguageValue = 'en' | 'pl' | 'de' | 'es' | 'fr'

const languageOptions = [
  { value: 'en', label: 'English' },
  { value: 'pl', label: 'Polish' },
  { value: 'de', label: 'Deutsch' },
  { value: 'es', label: 'Español' },
  { value: 'fr', label: 'Français' },
] as const satisfies readonly SelectOption<LanguageValue>[]

type SummaryFrequency = 'instant' | 'daily' | 'weekly'

const frequencyOptions = [
  { value: 'instant', label: 'Instant' },
  { value: 'daily', label: 'Daily' },
  { value: 'weekly', label: 'Weekly' },
] as const satisfies readonly RadioOption<SummaryFrequency>[]

function App() {
  const [name, setName] = useState('Anna Kowalska')
  const [email, setEmail] = useState('anna.kowalska@studio.dev')
  const [selectedSkills, setSelectedSkills] = useState<string[]>([
    'react',
    'typescript',
    'design-systems',
  ])
  const [emailNotifications, setEmailNotifications] = useState(true)
  const [pushNotifications, setPushNotifications] = useState(false)
  const [marketingEmails, setMarketingEmails] = useState(false)
  const [summaryFrequency, setSummaryFrequency] = useState<SummaryFrequency>('daily')
  const [language, setLanguage] = useState<LanguageValue>('en')
  const [fontSize, setFontSize] = useState(18)
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false)

  const selectedSkillLabels = useMemo(() => {
    const lookup = new Map(skillOptions.map((skill) => [skill.value, skill.label]))
    return selectedSkills.map((skill) => lookup.get(skill) ?? skill)
  }, [selectedSkills])

  const languageLabel = useMemo(
    () => languageOptions.find((option) => option.value === language)?.label ?? language,
    [language],
  )

  return (
    <Tooltip.Provider>
      <main className="dashboard-shell">
        <section className="hero-card">
          <div className="hero-copy">
            <p className="eyebrow">Base UI practice space</p>
            <h1>Settings Dashboard</h1>
            <p className="hero-text">
              Headless controls, custom styling and a compact settings surface tuned for
              desktop and mobile.
            </p>
          </div>

          <div className="hero-summary">
            <div className="summary-badge">
              <span>Language</span>
              <strong>{languageLabel}</strong>
            </div>
            <div className="summary-badge">
              <span>Font size</span>
              <strong>{fontSize}px</strong>
            </div>
            <div className="summary-badge">
              <span>Skills</span>
              <strong>{selectedSkillLabels.length}</strong>
            </div>
          </div>
        </section>

        <section className="dashboard-grid">
          <SettingsAccordion defaultValue={['profile', 'notifications', 'appearance']}>
            <Accordion.Item value="profile" className="settings-card">
              <Accordion.Header className="settings-accordion-header">
                <Accordion.Trigger className="settings-accordion-trigger">
                  <div>
                    <span className="section-title">Profile</span>
                    <span className="section-subtitle">
                      Basic identity data and interest tags.
                    </span>
                  </div>
                  <span className="accordion-caret" aria-hidden="true">
                    ▾
                  </span>
                </Accordion.Trigger>
              </Accordion.Header>

              <Accordion.Panel className="settings-accordion-panel">
                <div className="panel-grid">
                  <div className="field-stack">
                    <label className="field-label" htmlFor="profile-name">
                      Name
                    </label>
                    <input
                      id="profile-name"
                      className="text-input"
                      value={name}
                      onChange={(event) => setName(event.target.value)}
                      placeholder="Enter your name"
                    />
                  </div>

                  <div className="field-stack">
                    <label className="field-label" htmlFor="profile-email">
                      Email
                    </label>
                    <input
                      id="profile-email"
                      className="text-input"
                      type="email"
                      value={email}
                      onChange={(event) => setEmail(event.target.value)}
                      placeholder="name@example.com"
                    />
                  </div>

                  <SettingsCombobox
                    label="Skills and interests"
                    tooltip="Select multiple skills. Typing in the popup filters the list."
                    placeholder="Choose skills"
                    value={selectedSkills}
                    onValueChange={setSelectedSkills}
                    options={skillOptions}
                  />
                </div>
              </Accordion.Panel>
            </Accordion.Item>

            <Accordion.Item value="notifications" className="settings-card">
              <Accordion.Header className="settings-accordion-header">
                <Accordion.Trigger className="settings-accordion-trigger">
                  <div>
                    <span className="section-title">Notifications</span>
                    <span className="section-subtitle">
                      Delivery preferences and summary cadence.
                    </span>
                  </div>
                  <span className="accordion-caret" aria-hidden="true">
                    ▾
                  </span>
                </Accordion.Trigger>
              </Accordion.Header>

              <Accordion.Panel className="settings-accordion-panel">
                <div className="stacked-fields">
                  <SettingsSwitch
                    label="Email notifications"
                    description="Receive important account updates by email."
                    checked={emailNotifications}
                    onCheckedChange={setEmailNotifications}
                  />
                  <SettingsSwitch
                    label="Push notifications"
                    description="Show alerts immediately in supported browsers."
                    checked={pushNotifications}
                    onCheckedChange={setPushNotifications}
                  />
                  <SettingsSwitch
                    label="Marketing emails"
                    description="Occasional product updates and feature launches."
                    checked={marketingEmails}
                    onCheckedChange={setMarketingEmails}
                  />
                </div>

                <SettingsRadioGroup
                  label="Summary frequency"
                  description="Choose how often digest messages should arrive."
                  value={summaryFrequency}
                  onValueChange={setSummaryFrequency}
                  options={frequencyOptions}
                />
              </Accordion.Panel>
            </Accordion.Item>

            <Accordion.Item value="appearance" className="settings-card">
              <Accordion.Header className="settings-accordion-header">
                <Accordion.Trigger className="settings-accordion-trigger">
                  <div>
                    <span className="section-title">Appearance</span>
                    <span className="section-subtitle">
                      Interface language and typography scale.
                    </span>
                  </div>
                  <span className="accordion-caret" aria-hidden="true">
                    ▾
                  </span>
                </Accordion.Trigger>
              </Accordion.Header>

              <Accordion.Panel className="settings-accordion-panel">
                <div className="panel-grid">
                  <SettingsSelect
                    label="Language"
                    description="Used for interface labels and system messages."
                    value={language}
                    onValueChange={setLanguage}
                    options={languageOptions}
                    placeholder="Choose language"
                  />

                  <SettingsSlider
                    label="Font size"
                    tooltip="This changes the overall text scale of the dashboard preview."
                    description="Keep it comfortable for long reading sessions."
                    value={fontSize}
                    onValueChange={setFontSize}
                    min={14}
                    max={24}
                    step={1}
                    formatValue={(value) => `${value}px`}
                  />
                </div>
              </Accordion.Panel>
            </Accordion.Item>

            <Accordion.Item value="danger" className="settings-card danger-card">
              <Accordion.Header className="settings-accordion-header">
                <Accordion.Trigger className="settings-accordion-trigger">
                  <div>
                    <span className="section-title">Danger Zone</span>
                    <span className="section-subtitle">
                      Destructive action with explicit confirmation.
                    </span>
                  </div>
                  <span className="accordion-caret" aria-hidden="true">
                    ▾
                  </span>
                </Accordion.Trigger>
              </Accordion.Header>

              <Accordion.Panel className="settings-accordion-panel">
                <div className="danger-panel">
                  <div>
                    <h2>Delete account</h2>
                    <p>
                      This removes your workspace profile, saved preferences and local draft
                      data.
                    </p>
                  </div>

                  <button
                    type="button"
                    className="danger-button"
                    onClick={() => setDeleteDialogOpen(true)}
                  >
                    Delete account
                  </button>
                </div>
              </Accordion.Panel>
            </Accordion.Item>
          </SettingsAccordion>

          <aside className="preview-card">
            <div className="preview-header">
              <p className="eyebrow">Live snapshot</p>
              <h2>Current profile</h2>
            </div>

            <dl className="preview-list">
              <div>
                <dt>Name</dt>
                <dd>{name}</dd>
              </div>
              <div>
                <dt>Email</dt>
                <dd>{email}</dd>
              </div>
              <div>
                <dt>Selected skills</dt>
                <dd>{selectedSkillLabels.join(', ')}</dd>
              </div>
              <div>
                <dt>Summary cadence</dt>
                <dd>
                  {summaryFrequency === 'instant'
                    ? 'Instant'
                    : summaryFrequency === 'daily'
                      ? 'Daily'
                      : 'Weekly'}
                </dd>
              </div>
              <div>
                <dt>Notifications</dt>
                <dd>
                  {emailNotifications ? 'Email on' : 'Email off'} ·{' '}
                  {pushNotifications ? 'Push on' : 'Push off'}
                </dd>
              </div>
            </dl>
          </aside>
        </section>

        <SettingsConfirmationDialog
          open={deleteDialogOpen}
          onOpenChange={setDeleteDialogOpen}
          title="Delete this account?"
          description="This action is permanent. All local preferences and generated data will be removed."
          confirmLabel="Confirm"
          onConfirm={() => setDeleteDialogOpen(false)}
        />
      </main>
    </Tooltip.Provider>
  )
}

export default App
