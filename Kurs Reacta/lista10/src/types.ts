export type Role = 'admin' | 'guest';

export interface Book {
  id: string;
  title: string;
  author: string;
  year: number;
  description: string;
  coverImage?: string;
}
