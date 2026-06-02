# Test coverage plan

## Zaimplementowane teraz

| Obszar | Co testuje | Typ | Dlaczego |
| --- | --- | --- | --- |
| `src/lib/recipeReducer.ts` | Dodawanie, usuwanie i przełączanie ulubionych przepisów, w tym stabilne UUID dla dodawania | unit | To czysta logika bez DOM, więc unit daje najszybszy i najtańszy sygnał regresji |
| `src/components/RecipeForm.tsx` | Walidację pustego formularza i ścieżkę dodania przepisu widoczną w liście | browser | Komponent ma stan, formularz i interakcję z kontekstem, więc browser najlepiej oddaje perspektywę użytkownika |
| Główny flow aplikacji | Wejście na stronę, dodanie przepisu i zobaczenie go na ekranie | e2e | To najważniejsza ścieżka integrująca UI, kontekst i działający serwer deweloperski |

## Co jeszcze warto testować

| Obszar | Co testowałbym | Typ | Dlaczego |
| --- | --- | --- | --- |
| `src/lib/validateRecipe.ts` | Pusty tytuł, pustą treść i duplikaty tytułów | unit | Czysta funkcja, idealna do szybkich testów brzegowych |
| `src/lib/filterRecipes.ts` | Filtrowanie po frazie i trybie `favoritesOnly` | unit | Logika filtrowania jest deterministyczna i nie wymaga renderowania komponentów |
| `src/context/RecipeContext.tsx` | Integrację `addRecipe`, `deleteRecipe`, `toggleFavorite` oraz aktualizację widocznych przepisów | browser | Provider łączy reducer, walidację i filtrowanie, więc browser lepiej sprawdza realne zachowanie niż sam unit |
| `src/components/RecipeFilters.tsx` | Wyszukiwanie i przełącznik ulubionych tylko | browser | To interakcje UI sterujące widoczną listą, więc warto je sprawdzać z poziomu użytkownika |
| `src/components/RecipeList.tsx` | Stan pustej listy oraz render kart przepisów | browser | Komponent jest cienką warstwą widoku, więc browser wystarczy do sprawdzenia widocznego efektu |
| `src/components/RecipeCard.tsx` | Przyciski ulubionych i usuwania oraz oznaczenie ulubionego przepisu | browser | Zachowanie jest czysto UI-owe i zależy od dostępnych akcji użytkownika |
| `src/components/ThemeToggle.tsx` | Zmianę etykiety i dostępność przycisku trybu | browser | Stan tematu jest widoczny w UI, ale nie wymaga pełnego e2e |
| `src/hooks/useDarkMode.ts` | Odczyt i zapis preferencji motywu | browser | Hook korzysta z efektów i storage, więc browser daje sensowniejsze pokrycie niż unit bez DOM |
| `src/components/RecipeBoxApp.tsx` i `src/App.tsx` | Złożenie layoutu, providerów i podstawowego renderu strony | e2e albo browser | To bardziej integracja całej aplikacji niż logika biznesowa |
| `src/lib/getRandomUUID.ts` | Czy zwraca poprawnie identyfikator | unit | W praktyce wystarczy pośrednio przez test reducera, więc osobny test nie jest konieczny |
