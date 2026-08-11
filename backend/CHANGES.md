# Backend changes — frontend-to-backend recipe creation fix

## Overview

The "create a recipe" flow was broken end-to-end: the form payload didn't
match what the API expected, the API's storage path pointed at a directory
that no longer existed, and (discovered while testing the fix) saving a
recipe crashed the server. This pass fixes all three so a recipe submitted
from `recipes/new` actually gets validated, saved, and read back.

## What changed

### 1. Recipe model now matches the form (`app/models/recipe.py`)

`RecipeCreate`/`Recipe` required an `instructions: str` field that the
multi-step recipe form never sends. The form instead collects `ingredients`,
`tools`, `prep`, and `cook` as separate step lists. The model was reshaped to
match:

```python
class RecipeCreate(BaseModel):
    title: str
    ingredients: List[str]
    tools: List[str] = []
    prep: List[str]
    cook: List[str]
    category: Optional[str] = None
    tags: List[str] = []
```

`instructions` is gone; `tools`/`prep`/`cook` are new. `Recipe` (the
stored/returned shape) mirrors the same fields plus `id`, `created_at`,
`updated_at`.

### 2. Fixed the storage path (`app/db/json_handler.py`)

`DATA_DIR` was computed as `backend/app/db/../../data` = `backend/data` —
but that directory had already been deleted, and the comment claiming it
resolved to `backend/app/data` was wrong. Every read silently returned `[]`
and every write recreated the wrong directory. Fixed the relative path
(`../data` instead of `../../data`) so it correctly resolves to
`backend/app/data/recipes.json`, the file that's actually tracked and
populated.

### 3. Removed the second, unused storage layer

`app/crud/recipe_crud.py` was a second, never-imported implementation of
recipe load/save, using a relative path (`Path("app/data/recipes.json")`)
that only resolves correctly if the server process's *working directory* is
`backend/` at launch time — true when you run `uvicorn app.main:app` from
inside `backend/`, but not from the repo root, an IDE run config, or a
container with a different `WORKDIR`. `json_handler.py`'s approach
(anchoring the path to `os.path.abspath(__file__)`) doesn't have this
problem, so it's the one kept. Deleted `app/crud/recipe_crud.py` (and the
now-empty `crud/` dir) and a stray, unreferenced `app/db/recipes.json`.

### 4. Fixed a crash on every recipe save (`app/db/json_handler.py`)

Found while testing the above: `save_data()` passed Pydantic's `.dict()`
output straight to `json.dump()`. Python's stdlib `json` module can't
serialize `datetime` objects (`created_at`/`updated_at` are `datetime`), so
every `POST /recipes/` was throwing a 500 mid-write — and had already
corrupted `app/data/recipes.json` with a truncated partial write before this
fix. Added `default=str` to `json.dump()` so datetimes serialize as ISO-ish
strings instead of crashing. The corrupted data file was reset to `[]`.

## Verified

Ran the API locally and confirmed:
- `POST /recipes/` with the exact payload shape `recipes/new/page.tsx`
  sends (`title`, `ingredients`, `tools`, `prep`, `cook`) returns `200` with
  a fully populated recipe (id, timestamps included).
- `GET /recipes/` returns the saved recipe back.

## Known follow-ups (not done in this pass)

- `GET /tips` has no backend route yet — `tips/page.tsx` will still 404.
- `recipes/[id]/page.tsx` is a static placeholder; it doesn't fetch a
  recipe yet, and `api.ts` has no `fetchRecipe(id)` helper.
- `create_recipe`'s id assignment (`len(recipes) + 1`) will produce
  duplicate ids once a recipe is deleted and a new one is added.
- `recipes/new/page.tsx` calls `fetch` directly instead of going through
  `api.ts`; there's no `createRecipe()` helper there yet.
- `recipes/page.tsx` renders raw JSON (`<pre>`) instead of `RecipeCard`,
  which is currently an empty file.
