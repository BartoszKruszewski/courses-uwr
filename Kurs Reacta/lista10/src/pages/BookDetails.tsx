import { useParams, Link, useNavigate } from 'react-router-dom';
import { getBookById } from '../data/books';

export function BookDetails() {
  const { bookId } = useParams<{ bookId: string }>();
  const navigate = useNavigate();
  
  const book = getBookById(bookId || '');

  if (!book) {
    return (
      <div style={{ padding: '2rem' }}>
        <h2>Book not found</h2>
        <p>The book with ID "{bookId}" does not exist.</p>
        <button onClick={() => navigate('/books')}>Back to Catalog</button>
      </div>
    );
  }

  return (
    <div style={{ padding: '2rem', maxWidth: '600px', margin: '0 auto' }}>
      <Link to="/books" style={{ display: 'inline-block', marginBottom: '1rem' }}>&larr; Back to Catalog</Link>
      <div style={{ padding: '2rem', border: '1px solid #ddd', borderRadius: '8px', background: '#fff' }}>
        <h2 style={{ marginTop: 0 }}>{book.title}</h2>
        <h4 style={{ color: '#555' }}>by {book.author} ({book.year})</h4>
        <hr />
        <p style={{ lineHeight: '1.6' }}>{book.description}</p>
      </div>
    </div>
  );
}
