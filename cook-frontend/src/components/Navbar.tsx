// src/components/Navbar.tsx
import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full bg-white shadow-md p-4 mb-6">
      <ul className="flex gap-6">
        <li>
          <Link href="/">Home</Link>
        </li>
        <li>
          <Link href="/recipes">Recipes</Link>
        </li>
        <li>
          <Link href="/tips">Tips</Link>
        </li>
      </ul>
    </nav>
  );
}
