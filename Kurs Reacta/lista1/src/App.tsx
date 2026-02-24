import './App.css'
import AboutSection from './components/AboutSection'
import AppLayout from './components/AppLayout'
import ProfileCard from './components/ProfileCard'
import SkillsSection from './components/SkillsSection'
import profilePhoto from './assets/profile_photo.png'

const profile = {
  name: 'Jan Kowalski',
  role: 'Frontend Developer',
  avatarUrl: profilePhoto,
  contacts: [
    { label: 'Email', value: 'jan.kowalski@brightmail.pl', href: 'mailto:jan.kowalski@brightmail.pl' },
    { label: 'Telefon', value: '+48 555 123 987', href: 'tel:+48555123987' },
    { label: 'WWW', value: 'www.jankowalski.dev', href: 'https://www.jankowalski.dev' },
  ],
}

const aboutText =
  'Tworzę produkty cyfrowe, które łączą spójną narrację marki z przyjaznym doświadczeniem użytkownika. Na co dzień projektuję interfejsy, prototypuję w krótkich iteracjach i dbam o jakość kodu. Lubię łączyć analityczne podejście z empatią, dlatego w każdym projekcie prowadzę rozmowy z użytkownikami i przekuwam wnioski w konkretne decyzje projektowe.'

const skills = [
  'React + TypeScript',
  'Projektowanie UI w Figma',
  'Design systems',
  'Storybook',
  'Dostępność (WCAG)',
  'Animacje CSS',
  'Research użytkowników',
  'Warsztaty z klientem',
  'Praca z API REST',
]

function App() {
  return (
    <AppLayout>
      <ProfileCard
        name={profile.name}
        role={profile.role}
        avatarUrl={profile.avatarUrl}
        contacts={profile.contacts}
      />
      <div className="app-sections">
        <AboutSection text={aboutText} />
        <SkillsSection skills={skills} />
      </div>
    </AppLayout>
  )
}

export default App
