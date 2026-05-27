import { createTodo } from "../../actions";
import { TodoForm } from "../../components/TodoForm";
import Link from "next/link";

export default function NewTodoPage() {
  return (
    <div className="max-w-lg mx-auto">
      <div className="mb-6">
        <Link href="/todos" className="text-sm font-medium text-blue-600 hover:text-blue-800 flex items-center gap-1 w-fit">
          <span aria-hidden="true">&larr;</span> Back to Todos
        </Link>
      </div>
      <h2 className="text-2xl font-bold text-gray-900 tracking-tight text-center">Add New Todo</h2>
      <TodoForm action={createTodo} />
    </div>
  );
}
