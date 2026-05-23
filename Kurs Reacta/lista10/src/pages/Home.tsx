import { Link } from 'react-router-dom';

export function Home() {
  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h1>Welcome to the Book Library</h1>
      <p>This is a simple application demonstrating React Router features.</p>
      <p>You can browse our collection in the <Link to="/books">Catalog</Link>.</p>
    </div>
  );
}
