import { NavLink } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Navigation.css';

export function Navigation() {
  const { role, setRole } = useAuth();

  return (
    <nav className="main-nav">
      <div className="nav-links">
        <NavLink to="/" end className={({ isActive }) => isActive ? 'active' : ''}>Home</NavLink>
        <NavLink to="/books" className={({ isActive }) => isActive ? 'active' : ''}>Catalog</NavLink>
        {role === 'admin' && (
          <NavLink to="/admin" className={({ isActive }) => isActive ? 'active' : ''}>Admin</NavLink>
        )}
      </div>
      <div className="auth-controls">
        <span>Current Role: <strong>{role}</strong></span>
        {role === 'guest' ? (
          <button onClick={() => setRole('admin')}>Switch to Admin</button>
        ) : (
          <button onClick={() => setRole('guest')}>Switch to Guest</button>
        )}
      </div>
    </nav>
  );
}
