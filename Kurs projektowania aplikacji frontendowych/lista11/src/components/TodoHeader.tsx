import type { Action } from "../reducer/todoReducer";

interface Props {
    remaining: number;
    dispatch: React.Dispatch<Action>;
}

export default function TodoHeader({ remaining, dispatch }: Props) {
    return (
        <header className="todos-header__container">
            <h2>
                Todo List (<span>{remaining}</span> remaining)
                <button className="todos-clear" onClick={() => dispatch({ type: "clear" })}>
                    Clear all
                </button>
            </h2>
        </header>
    );
}
