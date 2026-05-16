import type { Todo } from '../types'
import { TodoItem } from './TodoItem'

type TodoListProps = {
  todos: Todo[]
  onToggle: (todo: Todo) => void
  onDelete: (id: string) => void
  disabled?: boolean
  busyTodoId?: string | null
  busyAction?: 'toggle' | 'delete' | null
}

export function TodoList({
  todos,
  onToggle,
  onDelete,
  disabled = false,
  busyTodoId = null,
  busyAction = null,
}: TodoListProps) {
  return (
    <ul className="space-y-3">
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={onToggle}
          onDelete={onDelete}
          disabled={disabled}
          isSaving={busyAction === 'toggle' && busyTodoId === todo.id}
          isDeleting={busyAction === 'delete' && busyTodoId === todo.id}
        />
      ))}
    </ul>
  )
}