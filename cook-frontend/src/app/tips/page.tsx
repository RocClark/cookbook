// src/app/tips/page.tsx
import { fetchTips } from "@/lib/api";

export default async function TipsPage() {
  const data = await fetchTips(); // { tips: [...] }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Seasonal Tips</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
