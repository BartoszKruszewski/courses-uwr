import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { RootLayout } from './layouts/RootLayout';
import { AdminLayout } from './layouts/AdminLayout';
import { Home } from './pages/Home';
import { Catalog } from './pages/Catalog';
import { BookDetails } from './pages/BookDetails';
import { AdminDashboard } from './pages/admin/AdminDashboard';
import { AdminBookForm } from './pages/admin/AdminBookForm';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<RootLayout />}>
            <Route index element={<Home />} />
            <Route path="books" element={<Catalog />} />
            <Route path="books/:bookId" element={<BookDetails />} />

            <Route path="admin" element={<AdminLayout />}>
              <Route index element={<AdminDashboard />} />
              <Route path="books/new" element={<AdminBookForm />} />
              <Route path="books/edit/:bookId" element={<AdminBookForm />} />
            </Route>

            <Route path="*" element={<Navigate to="/" replace />} />
          </Route>
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
