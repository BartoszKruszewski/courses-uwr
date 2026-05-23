import { Outlet } from 'react-router-dom';
import { Navigation } from '../components/Navigation';

export function RootLayout() {
  return (
    <div className="app-container">
      <header>
        <Navigation />
      </header>
      <main className="main-content">
        <Outlet />
      </main>
      <footer style={{ textAlign: 'center', padding: '1rem', borderTop: '1px solid #ddd', marginTop: 'auto' }}>
        <p>&copy; 2026 Book Library</p>
      </footer>
    </div>
  );
}
