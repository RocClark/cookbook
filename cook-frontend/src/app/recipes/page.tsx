// src/app/recipes/page.tsx
import { fetchRecipes } from "@/lib/api";

export default async function RecipesPage() {
  const data = await fetchRecipes(); // { recipes: [...] }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Recipes</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
