// src/app/layout.tsx
import "./globals.css";
import Navbar from "../components/Navbar";

export const metadata = {
  title: "Cookbook App",
  description: "A personal cookbook with recipes and seasonal tips",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="font-sans bg-gray-100">
        <Navbar />
        <main className="p-8">{children}</main>
      </body>
    </html>
  );
}
