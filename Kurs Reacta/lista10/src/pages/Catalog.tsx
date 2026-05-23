import { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { getBooks } from '../data/books';
import type { Book } from '../types';
import './Catalog.css';

export function Catalog() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [books, setBooks] = useState<Book[]>([]);

  const query = searchParams.get('query') || '';
  const sort = searchParams.get('sort') || 'title';

  useEffect(() => {
    setBooks(getBooks());
  }, []);

  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSearchParams(prev => {
      if (e.target.value) {
        prev.set('query', e.target.value);
      } else {
        prev.delete('query');
      }
      return prev;
    });
  };

  const handleSortChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSearchParams(prev => {
      prev.set('sort', e.target.value);
      return prev;
    });
  };

  const filteredAndSortedBooks = books
    .filter(book => book.title.toLowerCase().includes(query.toLowerCase()) || book.author.toLowerCase().includes(query.toLowerCase()))
    .sort((a, b) => {
      if (sort === 'year') {
        return b.year - a.year; // newest first
      }
      // default: title
      return a.title.localeCompare(b.title);
    });

  return (
    <div className="catalog-container">
      <h2>Book Catalog</h2>
      
      <div className="filters">
        <input 
          type="text" 
          placeholder="Search by title or author..." 
          value={query}
          onChange={handleSearchChange}
          className="search-input"
        />
        <select value={sort} onChange={handleSortChange} className="sort-select">
          <option value="title">Sort by Title (A-Z)</option>
          <option value="year">Sort by Year (Newest)</option>
        </select>
      </div>

      <div className="book-grid">
        {filteredAndSortedBooks.map(book => (
          <div key={book.id} className="book-card">
            <h3>{book.title}</h3>
            <p><strong>Author:</strong> {book.author}</p>
            <p><strong>Year:</strong> {book.year}</p>
            <Link to={`/books/${book.id}`} className="details-link">View Details</Link>
          </div>
        ))}
        {filteredAndSortedBooks.length === 0 && (
          <p>No books found matching your criteria.</p>
        )}
      </div>
    </div>
  );
}
