"use client";
import { useState } from "react";

export default function CreateRecipePage() {
  // Basic fields
  const [title, setTitle] = useState("");

  // Step arrays
  const [ingredients, setIngredients] = useState<string[]>([""]);
  const [tools, setTools] = useState<string[]>([""]);
  const [prepSteps, setPrepSteps] = useState<string[]>([""]);
  const [cookSteps, setCookSteps] = useState<string[]>([""]);

  // Step management
  const [step, setStep] = useState(1);

  // Messages
  const [message, setMessage] = useState("");

  // Helpers
  const updateList = (
    setter: React.Dispatch<React.SetStateAction<string[]>>,
    index: number,
    value: string,
  ) => {
    setter((prev) => prev.map((item, i) => (i === index ? value : item)));
  };

  const addListItem = (
    setter: React.Dispatch<React.SetStateAction<string[]>>,
  ) => {
    setter((prev) => [...prev, ""]);
  };

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setMessage("Submitting...");

    const recipeData = {
      title,
      ingredients,
      tools,
      prep: prepSteps,
      cook: cookSteps,
    };

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/recipes`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(recipeData),
      });

      const result = await res.json();
      console.log("Backend Response:", result);

      setMessage("Recipe Submitted!");
    } catch (error) {
      console.error("Error submitting:", error);
      setMessage("Something went wrong.");
    }
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Create New Recipe</h1>

      <form onSubmit={handleSubmit}>
        {/* Step Navigation */}
        <div style={{ marginBottom: "20px" }}>
          <button type="button" onClick={() => setStep(1)}>
            Part 1
          </button>
          <button type="button" onClick={() => setStep(2)}>
            Part 2
          </button>
          <button type="button" onClick={() => setStep(3)}>
            Part 3
          </button>
        </div>

        {/* STEP 1 — Ingredients + Tools */}
        {step === 1 && (
          <div>
            <h2>Ingredients & Tools</h2>

            <label>Recipe Title:</label>
            <input value={title} onChange={(e) => setTitle(e.target.value)} />

            <h3>Ingredients</h3>
            {ingredients.map((item, index) => (
              <input
                key={index}
                value={item}
                onChange={(e) =>
                  updateList(setIngredients, index, e.target.value)
                }
              />
            ))}
            <button type="button" onClick={() => addListItem(setIngredients)}>
              Add Ingredient
            </button>

            <h3>Tools</h3>
            {tools.map((tool, index) => (
              <input
                key={index}
                value={tool}
                onChange={(e) => updateList(setTools, index, e.target.value)}
              />
            ))}
            <button type="button" onClick={() => addListItem(setTools)}>
              Add Tool
            </button>
          </div>
        )}

        {/* STEP 2 — Prep */}
        {step === 2 && (
          <div>
            <h2>Prep Steps</h2>
            {prepSteps.map((step, index) => (
              <input
                key={index}
                value={step}
                onChange={(e) =>
                  updateList(setPrepSteps, index, e.target.value)
                }
              />
            ))}
            <button type="button" onClick={() => addListItem(setPrepSteps)}>
              Add Prep Step
            </button>
          </div>
        )}

        {/* STEP 3 — Cook */}
        {step === 3 && (
          <div>
            <h2>Cooking Process</h2>
            {cookSteps.map((step, index) => (
              <input
                key={index}
                value={step}
                onChange={(e) =>
                  updateList(setCookSteps, index, e.target.value)
                }
              />
            ))}
            <button type="button" onClick={() => addListItem(setCookSteps)}>
              Add Cooking Step
            </button>

            {/* Final Submit */}
            <button type="submit" style={{ marginTop: "20px" }}>
              Submit Recipe
            </button>
          </div>
        )}
      </form>

      {message && <p>{message}</p>}
    </div>
  );
}
