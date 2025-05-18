import type { Todo } from "../types/todo";
import type { Action } from "../reducer/todoReducer";
import TodoItem from "./TodoItem";

interface Props {
    todos: Todo[];
    dispatch: React.Dispatch<Action>;
}

export default function TodoList({ todos, dispatch }: Props) {
    return (
        <ul className="todos__list">
            {todos.map(todo => (
                <TodoItem key={todo.id} todo={todo} dispatch={dispatch} />
            ))}
        </ul>
    );
}
