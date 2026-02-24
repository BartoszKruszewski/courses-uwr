import ProfileHeader from './ProfileHeader'
import ContactList from './ContactList'
import './ProfileCard.css'

export interface ContactItemData {
  label: string
  value: string
  href?: string
}

interface ProfileCardProps {
  name: string
  role: string
  avatarUrl: string
  contacts: ContactItemData[]
}

function ProfileCard({ name, role, avatarUrl, contacts }: ProfileCardProps) {
  return (
    <section className="profile-card">
      <ProfileHeader name={name} role={role} avatarUrl={avatarUrl} />
      <ContactList items={contacts} />
    </section>
  )
}

export default ProfileCard
