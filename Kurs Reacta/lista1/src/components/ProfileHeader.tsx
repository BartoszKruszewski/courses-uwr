import './ProfileHeader.css'

interface ProfileHeaderProps {
  name: string
  role: string
  avatarUrl: string
}

function ProfileHeader({ name, role, avatarUrl }: ProfileHeaderProps) {
  return (
    <header className="profile-header">
      <img className="profile-header__avatar" src={avatarUrl} alt={name} />
      <div className="profile-header__info">
        <p className="profile-header__name">{name}</p>
        <p className="profile-header__role">{role}</p>
      </div>
    </header>
  )
}

export default ProfileHeader
