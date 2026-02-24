import ContactItem from './ContactItem'
import type { ContactItemData } from './ProfileCard'
import './ContactList.css'

interface ContactListProps {
  items: ContactItemData[]
}

function ContactList({ items }: ContactListProps) {
  return (
    <ul className="contact-list">
      {items.map((item) => (
        <ContactItem key={item.label} {...item} />
      ))}
    </ul>
  )
}

export default ContactList
