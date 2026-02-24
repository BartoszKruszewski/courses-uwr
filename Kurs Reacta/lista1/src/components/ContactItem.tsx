import './ContactItem.css'

interface ContactItemProps {
  label: string
  value: string
  href?: string
}

function ContactItem({ label, value, href }: ContactItemProps) {
  const content = href ? (
    <a className="contact-item__link" href={href}>
      {value}
    </a>
  ) : (
    <span className="contact-item__value">{value}</span>
  )

  return (
    <li className="contact-item">
      <span className="contact-item__label">{label}</span>
      {content}
    </li>
  )
}

export default ContactItem
