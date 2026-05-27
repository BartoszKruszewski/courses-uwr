import { notFound } from "next/navigation";
import Link from "next/link";
import { TodoForm } from "../../../components/TodoForm";
import { updateTodo } from "../../../actions";
import { getTodoById } from "../../../lib/api";

export default async function EditTodoPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  
  const todo = await getTodoById(id);

  if (!todo) {
    notFound();
  }

  const updateTodoWithId = updateTodo.bind(null, id);

  return (
    <div className="max-w-lg mx-auto">
      <div className="mb-6">
        <Link href={`/todos/${id}`} className="text-sm font-medium text-blue-600 hover:text-blue-800 flex items-center gap-1 w-fit">
          <span aria-hidden="true">&larr;</span> Back to Details
        </Link>
      </div>
      <h2 className="text-2xl font-bold text-gray-900 tracking-tight text-center">Edit Todo</h2>
      <TodoForm 
        action={updateTodoWithId} 
        initialData={{ text: todo.text, done: todo.done }} 
      />
    </div>
  );
}
