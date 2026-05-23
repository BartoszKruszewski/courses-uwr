import { createContext, useContext, useState, type ReactNode } from 'react';
import type { Role } from '../types';

interface AuthContextType {
  role: Role;
  setRole: (role: Role) => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [role, setRole] = useState<Role>(() => {
    return (localStorage.getItem('library_role') as Role) || 'guest';
  });

  const handleSetRole = (newRole: Role) => {
    setRole(newRole);
    localStorage.setItem('library_role', newRole);
  };

  return (
    <AuthContext.Provider value={{ role, setRole: handleSetRole }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
