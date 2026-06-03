# Architecture — Todo List App

## Full-stack component diagram

```
Browser (HTML / CSS / JS)
         │
         │  fetch()
         ▼
┌──────────────────────────────────────┐
│  UI Layer  (ui/)                     │
│                                      │
│  index.html                          │
│  └── src/                            │
│      ├── api/client.js               │  fetch wrapper + error normalisation
│      ├── utils/state.js              │  in-memory app state + event bus
│      └── components/                 │
│          ├── TodoForm.js             │  add-todo form
│          ├── FilterBar.js            │  status tabs + keyword search
│          ├── TodoList.js             │  list + TodoItem
│          └── Toast.js               │  error notification
└──────────────────┬───────────────────┘
                   │  HTTP  /api/v1/…
                   ▼
┌──────────────────────────────────────┐
│  FastAPI  (src/)                     │
│                                      │
│  GET /          → serves index.html  │
│  GET /ui/…      → serves static JS  │
│  /api/v1/todos  → JSON API           │
└────────────┬─────────────────────────┘
             │
    ┌────────▼────────┐
    │     Router      │  validate input (Pydantic), HTTP concerns only
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │     Service     │  business logic, raises HTTPException
    └────────┬────────┘
             │
    ┌────────▼────────┐
    │   Repository    │  database operations only, no business logic
    └────────┬────────┘
             │
          SQLite  (via SQLAlchemy async)
```

---

## UI component tree

```
App  (state owner — bootstrapped in index.html)
├── Header         title + live todo count badge
├── FilterBar      All / Pending / Done tabs  +  keyword search input
├── TodoForm       title input  +  Add button  +  validation error
└── TodoList
    ├── Skeleton   3 placeholder cards shown while loading
    ├── EmptyState shown when the list is empty
    └── TodoItem[] (one per todo)
        ├── Checkbox      toggle pending ↔ done
        ├── TitleSpan     double-click to enter inline-edit mode
        └── DeleteButton  remove the todo
```

---

## UI data flow

1. App boots → `api.listTodos()` → `setState({ todos })` → TodoList renders
2. User submits form → `api.createTodo()` → re-fetch → `setState({ todos })`
3. User toggles checkbox → `api.updateTodo(id, { status })` → re-fetch
4. User deletes item → `api.deleteTodo(id)` → re-fetch
5. User changes filter / types in search → `api.listTodos({ status, q })` → re-fetch
6. Any API error → `setState({ error })` → Toast renders for 3 s

---

## Backend serves the UI

`src/main.py` mounts `StaticFiles` pointed at the `ui/` directory:

- `GET /`       → `ui/index.html`
- `GET /ui/…`   → files under `ui/`

---

## Database schema — `todos` table

| Column        | Type      | Notes                       |
|---------------|-----------|-----------------------------|
| `id`          | INTEGER   | Primary key, autoincrement  |
| `title`       | TEXT      | Not null                    |
| `description` | TEXT      | Nullable                    |
| `status`      | TEXT      | `"pending"` / `"done"`      |
| `created_at`  | DATETIME  | Server-side default (now)   |
| `updated_at`  | DATETIME  | Auto-updated on change      |

---

## File layout

```
todo-starter/
├── CLAUDE.md                      AI context — read this first every session
├── .env.example
├── requirements.txt
├── pyproject.toml
│
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── API_CONTRACT.md
│   ├── UI_SPEC.md
│   └── adr/
│       ├── ADR-001-sqlite-over-postgres.md
│       └── ADR-002-vanilla-js.md
│
├── prompts/                       Reusable AI prompts for TDD workflow
│   ├── generate-backend-test.md
│   ├── implement-backend.md
│   ├── generate-e2e-test.md
│   ├── implement-ui.md
│   └── review-code.md
│
├── src/                           FastAPI backend
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   └── todo.py
│   ├── schemas/
│   │   └── todo.py
│   ├── repositories/
│   │   └── todo_repository.py
│   ├── services/
│   │   └── todo_service.py
│   └── routers/
│       └── todo_router.py
│
├── ui/                            Vanilla JS frontend
│   ├── index.html
│   └── src/
│       ├── api/
│       │   └── client.js
│       ├── utils/
│       │   └── state.js
│       └── components/
│           ├── TodoForm.js
│           ├── FilterBar.js
│           ├── TodoList.js
│           └── Toast.js
│
└── tests/
    ├── conftest.py                shared fixtures (in-memory DB, test client)
    ├── unit/
    │   └── test_todos.py          backend unit tests (pytest + httpx)
    └── e2e/
        └── test_ui_todos.py       UI e2e tests (Playwright)
```
