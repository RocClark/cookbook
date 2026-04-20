export default async function Home() {
  console.log("ENV TEST:", process.env.NEXT_PUBLIC_API_URL);
  console.log("FOO:", process.env.FOO);

  return (
    <div>
      <h1>Home Page Working!</h1>
    </div>
  );
}
