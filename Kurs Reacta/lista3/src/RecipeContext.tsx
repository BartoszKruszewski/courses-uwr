import {
  createContext,
  useContext,
  useReducer,
  type ReactNode,
} from "react";

export interface Recipe {
  id: number;
  title: string;
  content: string;
  favorite: boolean;
}

type Action =
  | { type: "ADD_RECIPE"; payload: { title: string; content: string } }
  | { type: "DELETE_RECIPE"; payload: { id: number } }
  | { type: "TOGGLE_FAVORITE"; payload: { id: number } };

interface RecipeState {
  recipes: Recipe[];
  nextId: number;
}

const initialState: RecipeState = {
  recipes: [],
  nextId: 1,
};

function recipeReducer(state: RecipeState, action: Action): RecipeState {
  switch (action.type) {
    case "ADD_RECIPE":
      return {
        ...state,
        recipes: [
          ...state.recipes,
          {
            id: state.nextId,
            title: action.payload.title,
            content: action.payload.content,
            favorite: false,
          },
        ],
        nextId: state.nextId + 1,
      };
    case "DELETE_RECIPE":
      return {
        ...state,
        recipes: state.recipes.filter((r) => r.id !== action.payload.id),
      };
    case "TOGGLE_FAVORITE":
      return {
        ...state,
        recipes: state.recipes.map((r) =>
          r.id === action.payload.id ? { ...r, favorite: !r.favorite } : r
        ),
      };
  }
}

interface RecipeContextValue {
  recipes: Recipe[];
  dispatch: React.Dispatch<Action>;
}

const RecipeContext = createContext<RecipeContextValue | null>(null);

export function RecipeProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(recipeReducer, initialState);

  return (
    <RecipeContext.Provider value={{ recipes: state.recipes, dispatch }}>
      {children}
    </RecipeContext.Provider>
  );
}

export function useRecipes(): RecipeContextValue {
  const ctx = useContext(RecipeContext);
  if (!ctx) {
    throw new Error("useRecipes must be used within a RecipeProvider");
  }
  return ctx;
}
