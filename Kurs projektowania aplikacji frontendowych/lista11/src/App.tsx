import { useReducer } from "react";
import { todoReducer } from "./reducer/todoReducer";
import TodoHeader from "./components/TodoHeader";
import AddTodoForm from "./components/AddTodoForm";
import TodoList from "./components/TodoList";

export default function App() {
    const [todos, dispatch] = useReducer(todoReducer, []);
    const remaining = todos.filter(t => !t.completed).length;

    return (
        <div className="body__wrapper">
            <header className="header__wrapper">
                <h1>Hello!</h1>
            </header>

            <main className="main">
                <AddTodoForm dispatch={dispatch} />
                <section className="todos__container">
                    <TodoHeader remaining={remaining} dispatch={dispatch} />
                    <TodoList todos={todos} dispatch={dispatch} />
                </section>
            </main>
        </div>
    );
}
