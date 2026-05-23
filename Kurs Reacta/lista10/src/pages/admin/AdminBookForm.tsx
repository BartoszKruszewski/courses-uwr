import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getBookById, getBooks, saveBooks } from '../../data/books';
import type { Book } from '../../types';

export function AdminBookForm() {
  const { bookId } = useParams<{ bookId: string }>();
  const navigate = useNavigate();
  const isEditMode = Boolean(bookId);

  const [formData, setFormData] = useState<Partial<Book>>({
    title: '',
    author: '',
    year: new Date().getFullYear(),
    description: ''
  });

  useEffect(() => {
    if (isEditMode && bookId) {
      const book = getBookById(bookId);
      if (book) {
        setFormData(book);
      } else {
        alert('Book not found!');
        navigate('/admin');
      }
    }
  }, [bookId, isEditMode, navigate]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: name === 'year' ? parseInt(value) || '' : value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const books = getBooks();

    if (isEditMode) {
      const updatedBooks = books.map(b => b.id === bookId ? { ...b, ...formData } as Book : b);
      saveBooks(updatedBooks);
    } else {
      const newBook: Book = {
        ...formData,
        id: Date.now().toString(),
      } as Book;
      saveBooks([...books, newBook]);
    }
    navigate('/admin');
  };

  return (
    <div style={{ maxWidth: '600px' }}>
      <h2>{isEditMode ? 'Edit Book' : 'Add New Book'}</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Title:</label>
          <input 
            type="text" 
            name="title" 
            value={formData.title} 
            onChange={handleChange} 
            required 
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Author:</label>
          <input 
            type="text" 
            name="author" 
            value={formData.author} 
            onChange={handleChange} 
            required 
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Year:</label>
          <input 
            type="number" 
            name="year" 
            value={formData.year} 
            onChange={handleChange} 
            required 
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div>
          <label style={{ display: 'block', marginBottom: '0.5rem' }}>Description:</label>
          <textarea 
            name="description" 
            value={formData.description} 
            onChange={handleChange} 
            required 
            rows={5}
            style={{ width: '100%', padding: '0.5rem' }}
          />
        </div>
        <div style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
          <button type="submit" style={{ padding: '0.5rem 1rem', background: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
            {isEditMode ? 'Save Changes' : 'Create Book'}
          </button>
          <button type="button" onClick={() => navigate('/admin')} style={{ padding: '0.5rem 1rem', background: '#6c757d', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}
