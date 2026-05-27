"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export function Nav() {
  const pathname = usePathname();

  return (
    <nav className="bg-white shadow border-b border-gray-200 mb-8">
      <div className="max-w-4xl mx-auto px-4">
        <ul className="flex space-x-8 py-4 text-sm font-medium">
          <li>
            <Link
              href="/"
              className={`hover:text-blue-600 transition-colors ${pathname === "/" ? "text-blue-600" : "text-gray-600"}`}
            >
              Home
            </Link>
          </li>
          <li>
            <Link
              href="/todos"
              className={`hover:text-blue-600 transition-colors ${pathname.startsWith("/todos") ? "text-blue-600" : "text-gray-600"}`}
            >
              Todos
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}
