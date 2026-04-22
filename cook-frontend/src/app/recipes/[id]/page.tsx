// src/app/recipes/[id]/page.tsx
export default function RecipeDetailPage({
  params,
}: {
  params: { id: string };
}) {
  return (
    <div>
      <h1 className="text-2xl font-bold">Recipe ID: {params.id}</h1>
      <p className="text-gray-700 mt-4">
        This page will later fetch and show a single recipe.
      </p>
    </div>
  );
}
