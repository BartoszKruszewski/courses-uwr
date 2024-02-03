type User = {
  name: string;
  age: number;
  occupation?: string;
};

type Admin = {
  name: string;
  age: number;
  role?: string;
};

export type Person = User & Admin;

export const persons: Person[] = [
  {
    name: "Jan Kowalski",
    age: 17,
    occupation: "Student",
  },
  {
    name: "Tomasz Malinowski",
    age: 20,
    role: "Administrator",
  },
];
