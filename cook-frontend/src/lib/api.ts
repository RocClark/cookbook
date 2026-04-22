// src/lib/api.ts
const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function fetchRecipes() {
  const res = await fetch(`${API_URL}/recipes`, { cache: "no-store" });
  return res.json();
}

export async function fetchTips() {
  const res = await fetch(`${API_URL}/tips`, { cache: "no-store" });
  return res.json();
}
