import type { Book } from '../types';

const INITIAL_BOOKS: Book[] = [
  {
    id: '1',
    title: 'The Hobbit',
    author: 'J.R.R. Tolkien',
    year: 1937,
    description: "A fantasy novel and children's book by English author J. R. R. Tolkien."
  },
  {
    id: '2',
    title: '1984',
    author: 'George Orwell',
    year: 1949,
    description: 'A dystopian social science fiction novel and cautionary tale.'
  },
  {
    id: '3',
    title: 'To Kill a Mockingbird',
    author: 'Harper Lee',
    year: 1960,
    description: 'A novel by Harper Lee published in 1960. Instantly successful, widely read in high schools and middle schools in the United States, it has become a classic of modern American literature.'
  },
  {
    id: '4',
    title: 'The Great Gatsby',
    author: 'F. Scott Fitzgerald',
    year: 1925,
    description: 'A 1925 novel written by American author F. Scott Fitzgerald that follows a cast of characters living in the fictional towns of West Egg and East Egg on prosperous Long Island in the summer of 1922.'
  },
  {
    id: '5',
    title: 'Pride and Prejudice',
    author: 'Jane Austen',
    year: 1813,
    description: 'An 1813 romantic novel of manners written by Jane Austen. The novel follows the character development of Elizabeth Bennet, the dynamic protagonist of the book.'
  }
];

export const getBooks = (): Book[] => {
  const books = localStorage.getItem('library_books');
  if (books) {
    return JSON.parse(books);
  }
  localStorage.setItem('library_books', JSON.stringify(INITIAL_BOOKS));
  return INITIAL_BOOKS;
};

export const saveBooks = (books: Book[]) => {
  localStorage.setItem('library_books', JSON.stringify(books));
};

export const getBookById = (id: string): Book | undefined => {
  const books = getBooks();
  return books.find(b => b.id === id);
};
