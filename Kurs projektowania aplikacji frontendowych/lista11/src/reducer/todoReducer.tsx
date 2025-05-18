import type { Todo } from "../types/todo";

export type Action =
    | { type: "add"; name: string }
    | { type: "remove"; id: string }
    | { type: "toggle"; id: string }
    | { type: "clear" }
    | { type: "move_up"; id: string }
    | { type: "move_down"; id: string };

export function todoReducer(state: Todo[], action: Action): Todo[] {
    switch (action.type) {
        case "add":
            return [...state, { id: crypto.randomUUID(), name: action.name, completed: false }];

        case "remove":
            return state.filter(todo => todo.id !== action.id);

        case "toggle":
            return state.map(todo =>
                todo.id === action.id ? { ...todo, completed: !todo.completed } : todo
            );

        case "clear":
            return [];

        case "move_up": {
            const idx = state.findIndex(t => t.id === action.id);
            if (idx > 0) {
                const copy = [...state];
                [copy[idx - 1], copy[idx]] = [copy[idx], copy[idx - 1]];
                return copy;
            }
            return state;
        }

        case "move_down": {
            const idx = state.findIndex(t => t.id === action.id);
            if (idx >= 0 && idx < state.length - 1) {
                const copy = [...state];
                [copy[idx], copy[idx + 1]] = [copy[idx + 1], copy[idx]];
                return copy;
            }
            return state;
        }

        default:
            return state;
    }
}
