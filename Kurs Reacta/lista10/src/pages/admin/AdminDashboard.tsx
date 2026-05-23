import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getBooks, saveBooks } from '../../data/books';
import type { Book } from '../../types';

export function AdminDashboard() {
  const [books, setBooks] = useState<Book[]>([]);

  useEffect(() => {
    setBooks(getBooks());
  }, []);

  const handleDelete = (id: string) => {
    if (window.confirm('Are you sure you want to delete this book?')) {
      const updatedBooks = books.filter(b => b.id !== id);
      saveBooks(updatedBooks);
      setBooks(updatedBooks);
    }
  };

  return (
    <div>
      <h2>Manage Books</h2>
      <Link to="/admin/books/new" style={{ display: 'inline-block', marginBottom: '1rem', padding: '0.5rem 1rem', background: '#28a745', color: 'white', textDecoration: 'none', borderRadius: '4px' }}>
        Add New Book
      </Link>
      <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '1rem' }}>
        <thead>
          <tr style={{ background: '#f8f9fa', borderBottom: '2px solid #ddd' }}>
            <th style={{ padding: '0.75rem', textAlign: 'left' }}>Title</th>
            <th style={{ padding: '0.75rem', textAlign: 'left' }}>Author</th>
            <th style={{ padding: '0.75rem', textAlign: 'left' }}>Year</th>
            <th style={{ padding: '0.75rem', textAlign: 'left' }}>Actions</th>
          </tr>
        </thead>
        <tbody>
          {books.map(book => (
            <tr key={book.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={{ padding: '0.75rem' }}>{book.title}</td>
              <td style={{ padding: '0.75rem' }}>{book.author}</td>
              <td style={{ padding: '0.75rem' }}>{book.year}</td>
              <td style={{ padding: '0.75rem' }}>
                <Link to={`/admin/books/edit/${book.id}`} style={{ marginRight: '1rem', color: '#007bff' }}>Edit</Link>
                <button 
                  onClick={() => handleDelete(book.id)}
                  style={{ background: 'none', border: 'none', color: '#dc3545', cursor: 'pointer', textDecoration: 'underline' }}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
          {books.length === 0 && (
            <tr>
              <td colSpan={4} style={{ padding: '1rem', textAlign: 'center' }}>No books available.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
