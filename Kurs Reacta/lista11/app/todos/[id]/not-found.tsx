import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center py-16 text-center">
      <h2 className="text-3xl font-extrabold text-gray-900 mb-2">Not Found</h2>
      <p className="text-lg text-gray-600 mb-8">Could not find the requested resource</p>
      <Link 
        href="/todos"
        className="inline-flex justify-center rounded-md bg-blue-600 px-6 py-3 text-sm font-semibold text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 transition-colors"
      >
        Return to Todos
      </Link>
    </div>
  );
}
