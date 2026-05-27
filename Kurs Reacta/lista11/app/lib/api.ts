import { Todo } from "../types";

const API_URL = process.env.API_URL || "http://localhost:3001";

export async function getTodos(): Promise<Todo[]> {
  const res = await fetch(`${API_URL}/todos`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error("Failed to fetch todos");
  }
  return res.json();
}

export async function getTodoById(id: string): Promise<Todo | undefined> {
  const todos = await getTodos();
  return todos.find((t) => t.id === id);
}

export async function submitTodo(data: { text: string; done?: boolean }, method = "POST", id?: string) {
  const url = id ? `${API_URL}/todos/${id}` : `${API_URL}/todos`;
  const res = await fetch(url, {
    method,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: data.text,
      done: data.done ?? false,
    }),
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => null);
    throw new Error(errorData?.error || `Failed to ${method === "POST" ? "create" : "update"} todo`);
  }
  return res.json();
}
