import Link from "next/link";
import { Suspense } from "react";
import { toggleTodoStatus } from "../actions";
import { getTodos } from "../lib/api";
import { TodoBadge } from "../components/TodoBadge";

async function TodoList({ done }: { done?: string }) {
  let todos = await getTodos();
  
  if (done === "true") {
    todos = todos.filter(t => t.done === true);
  } else if (done === "false") {
    todos = todos.filter(t => t.done === false);
  }

  if (todos.length === 0) {
    return <p className="text-gray-600 py-8 text-center italic">No todos found.</p>;
  }

  return (
    <ul className="divide-y divide-gray-200 mt-4 border-t border-gray-200">
      {todos.map(todo => {
        const toggleAction = toggleTodoStatus.bind(null, todo.id, todo.text, todo.done);

        return (
          <li key={todo.id} className="py-4 flex flex-col sm:flex-row sm:items-center justify-between hover:bg-gray-50 px-2 -mx-2 rounded transition-colors group gap-2">
            <Link 
              href={`/todos/${todo.id}`} 
              className={`text-lg group-hover:text-blue-600 flex-grow ${todo.done ? "line-through text-gray-400" : "text-gray-900 font-medium"}`}
            >
              {todo.text}
            </Link>
            
            <div className="flex-shrink-0 flex items-center gap-3">
              <TodoBadge done={todo.done} />
              
              <form action={toggleAction}>
                <button 
                  type="submit" 
                  className={`px-3 py-1 text-xs font-medium rounded-md shadow-sm transition-colors border ${
                    todo.done 
                    ? "bg-white text-gray-700 border-gray-300 hover:bg-gray-50" 
                    : "bg-blue-50 text-blue-700 border-blue-200 hover:bg-blue-100"
                  }`}
                >
                  {todo.done ? "Mark Active" : "Mark Completed"}
                </button>
              </form>
            </div>
          </li>
        );
      })}
    </ul>
  );
}

function FilterTabs({ activeDone }: { activeDone?: string }) {
  const tabs = [
    { label: "All", value: undefined },
    { label: "Completed", value: "true" },
    { label: "Active", value: "false" },
  ];

  return (
    <div className="flex gap-2 mb-6 bg-gray-100 p-1 rounded-lg w-max">
      {tabs.map(tab => {
        const isActive = activeDone === tab.value;
        const href = tab.value ? `/todos?done=${tab.value}` : "/todos";
        return (
          <Link 
            key={tab.label}
            href={href} 
            className={`px-4 py-1.5 rounded-md text-sm font-medium transition-colors ${isActive ? "bg-white text-blue-600 shadow-sm" : "text-gray-600 hover:text-gray-900"}`}
          >
            {tab.label}
          </Link>
        );
      })}
    </div>
  );
}

export default async function TodosPage({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>;
}) {
  const doneParams = (await searchParams).done;
  const done = typeof doneParams === "string" ? doneParams : undefined;

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-extrabold text-gray-900 tracking-tight">Todos</h1>
        <Link 
          href="/todos/new" 
          className="inline-flex justify-center rounded-md bg-blue-600 py-2 px-4 text-sm font-semibold text-white shadow-sm hover:bg-blue-700 transition"
        >
          Add Todo +
        </Link>
      </div>
      
      <FilterTabs activeDone={done} />

      <Suspense fallback={<p className="text-gray-600 py-8 animate-pulse text-center">Loading list...</p>} key={done || "all"}>
        <TodoList done={done} />
      </Suspense>
    </div>
  );
}
