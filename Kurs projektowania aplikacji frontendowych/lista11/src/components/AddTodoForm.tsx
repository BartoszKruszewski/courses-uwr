import { useState, type FormEvent } from "react";
import type { Action } from "../reducer/todoReducer";

interface Props {
    dispatch: React.Dispatch<Action>;
}

export default function AddTodoForm({ dispatch }: Props) {
    const [name, setName] = useState("");

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        if (!name.trim()) return;
        dispatch({ type: "add", name: name.trim() });
        setName("");
    };

    return (
        <form onSubmit={handleSubmit} className="add-item__container" id="add-todo-form">
            <input
                className="add-item__element add-item__input"
                placeholder="What's on your mind?"
                aria-label="add todo"
                required
                value={name}
                onChange={e => setName(e.target.value)}
            />
            <button type="submit" className="add-item__element add-item__submit">
                Add
            </button>
        </form>
    );
}
