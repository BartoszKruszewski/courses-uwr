import "./App.css";
import { RecipeProvider } from "./RecipeContext";
import RecipeForm from "./components/RecipeForm";
import RecipeList from "./components/RecipeList";

function App() {
  return (
    <RecipeProvider>
      <div className="app">
        <header className="app-header">
          <h1>Recipe Book</h1>
          <p>Collect &amp; organize your favorite recipes</p>
        </header>
        <RecipeForm />
        <RecipeList />
      </div>
    </RecipeProvider>
  );
}

export default App;
