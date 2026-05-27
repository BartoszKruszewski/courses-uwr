import { notFound } from "next/navigation";
import Link from "next/link";
import { getTodoById } from "../../lib/api";
import { TodoBadge } from "../../components/TodoBadge";

export default async function TodoDetailsPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  
  const todo = await getTodoById(id);

  if (!todo) {
    notFound();
  }

  return (
    <div className="max-w-xl mx-auto">
      <div className="mb-6">
        <Link href="/todos" className="text-sm font-medium text-blue-600 hover:text-blue-800 flex items-center gap-1 w-fit">
          <span aria-hidden="true">&larr;</span> Back to Todos
        </Link>
      </div>
      
      <div className="bg-gray-50 border border-gray-200 rounded-lg p-6 sm:p-8 shadow-sm">
        <div className="flex justify-between items-start gap-4 mb-6">
          <h2 className={`text-2xl font-bold ${todo.done ? "text-gray-500 line-through" : "text-gray-900"}`}>
            {todo.text}
          </h2>
          <TodoBadge done={todo.done} />
        </div>
        
        <div className="pt-6 border-t border-gray-200 mt-8">
          <Link 
            href={`/todos/${id}/edit`} 
            className="inline-flex justify-center rounded-md bg-white px-4 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 transition w-full sm:w-auto"
          >
            Edit Todo
          </Link>
        </div>
      </div>
    </div>
  );
}
