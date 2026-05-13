import type { Todo } from './types'

const API_URL = 'http://localhost:3001'

async function requestJson<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...(init?.headers ?? {}),
    },
  })

  const contentType = response.headers.get('content-type') ?? ''
  const payload = contentType.includes('application/json')
    ? await response.json()
    : await response.text()

  if (!response.ok) {
    const message =
      payload && typeof payload === 'object' && 'error' in payload
        ? String((payload as { error?: unknown }).error ?? 'Błąd API')
        : `Błąd API (${response.status})`

    throw new Error(message)
  }

  return payload as T
}

export function getTodos() {
  return requestJson<Todo[]>('/todos')
}

export function createTodo(text: string) {
  return requestJson<Todo>('/todos', {
    method: 'POST',
    body: JSON.stringify({ text }),
  })
}

export function updateTodo(id: string, todo: Pick<Todo, 'text' | 'done'>) {
  return requestJson<Todo>(`/todos/${id}`, {
    method: 'PUT',
    body: JSON.stringify(todo),
  })
}

export function deleteTodo(id: string) {
  return requestJson<Todo>(`/todos/${id}`, {
    method: 'DELETE',
  })
}