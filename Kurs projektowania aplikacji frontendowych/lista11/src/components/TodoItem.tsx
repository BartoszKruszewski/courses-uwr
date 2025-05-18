import type { Todo } from "../types/todo";
import type { Action } from "../reducer/todoReducer";

interface Props {
    todo: Todo;
    dispatch: React.Dispatch<Action>;
}

export default function TodoItem({ todo, dispatch }: Props) {
    const { id, name, completed } = todo;

    return (
        <li className={`todo__container ${completed ? "todo__container--completed" : ""}`}>
            <div className="todo-element todo-name">{name}</div>

            <button
                className="todo-element todo-button move-up"
                onClick={() => dispatch({ type: "move_up", id })}
            >
                ↑
            </button>

            <button
                className="todo-element todo-button move-down"
                onClick={() => dispatch({ type: "move_down", id })}
            >
                ↓
            </button>

            {!completed ? (
                <button
                    className="todo-element todo-button"
                    onClick={() => dispatch({ type: "toggle", id })}
                >
                    Done
                </button>
            ) : (
                <button
                    className="todo-element todo-button"
                    onClick={() => dispatch({ type: "toggle", id })}
                >
                    Revert
                </button>
            )}

            <button
                className="todo-element todo-button"
                onClick={() => dispatch({ type: "remove", id })}
            >
                Remove
            </button>
        </li>
    );
}
