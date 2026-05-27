import Link from "next/link";

export default function Home() {
  return (
    <div className="text-center py-16">
      <h1 className="text-4xl font-extrabold text-gray-900 mb-4 tracking-tight">Welcome to the ToDo App</h1>
      <p className="text-lg text-gray-600 mb-8 max-w-md mx-auto">
        This is a simple ToDo application built with Next.js App Router and Server Actions. Manage your daily tasks efficiently.
      </p>
      <Link 
        href="/todos" 
        className="inline-flex items-center justify-center rounded-md bg-blue-600 px-6 py-3 text-sm font-medium text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-colors"
      >
        View Todos
      </Link>
    </div>
  );
}
