# Todo List App — Starter

A full-stack todo application skeleton for practicing TDD with an AI coding agent.
**No implementation code is included.** Every source file contains only `TODO` comments
describing what to build. The tests are already written and waiting to fail.

---

## What's in this project

```
todo-starter/
├── CLAUDE.md                       AI context — Claude Code reads this automatically
├── docs/
│   ├── PRD.md                      Requirements and acceptance criteria
│   ├── ARCHITECTURE.md             Full-stack component design and data flow
│   ├── API_CONTRACT.md             Endpoint specifications
│   ├── UI_SPEC.md                  UI components and interaction design
│   └── adr/                        Architecture decision records
├── prompts/
│   ├── implement-backend.md        AI prompt for the Green phase (backend)
│   ├── implement-ui.md             AI prompt for the Green phase (UI)
│   └── review-code.md              AI prompt for post-implementation review
├── src/                            FastAPI backend — stubs only, no implementation
├── ui/                             Vanilla JS frontend — stubs only, no implementation
└── tests/
    ├── conftest.py                 Shared fixtures (in-memory SQLite, test client)
    ├── unit/test_todos.py          16 backend tests — ready to run
    └── e2e/test_ui_todos.py        12 Playwright UI tests — ready to run
```

---

## Prerequisites

- Python 3.11+
- Node.js is **not** required (no JS build step)
- A Claude account with access to Claude Code

---

## Install Claude Code

Choose the method that suits your OS:

```bash
# Native binary (recommended)
curl -fsSL https://claude.ai/install.sh | bash

# macOS with Homebrew
brew install --cask claude-code

# npm (deprecated but still works)
npm install -g @anthropic-ai/claude-code
```

Verify the installation:

```bash
claude --version
```

---

## Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## TDD workflow

This project follows the Red → Green → Refactor cycle.
The tests are the specification. Implement only enough code to make them pass.

### Step 1 — confirm the tests fail (Red)

```bash
pytest tests/unit/ -v
# Expected: 16 FAILED — no implementation exists yet
```

### Step 2 — open Claude Code

```bash
cd todo-starter
claude
# Claude Code reads CLAUDE.md automatically on startup
```

### Step 3 — implement the backend layer by layer (Green)

Send one prompt per layer. Always ask Claude to run the tests after each step.

```
> run pytest tests/unit/ -v and show me which tests fail

> implement src/models/todo.py then run pytest tests/unit/ -v

> implement src/schemas/todo.py then run pytest tests/unit/ -v

> implement src/database.py and src/config.py then run pytest tests/unit/ -v

> implement src/repositories/todo_repository.py then run pytest tests/unit/ -v

> implement src/services/todo_service.py then run pytest tests/unit/ -v

> implement src/routers/todo_router.py and src/main.py then run pytest tests/unit/ -v
```

Target: **16 passed**.

### Step 4 — implement the UI layer by layer (Green)

```bash
playwright install chromium    # one-time setup for e2e tests
```

```
> implement ui/src/utils/state.js and ui/src/api/client.js

> implement ui/src/components/Toast.js then run pytest tests/e2e/ -v

> implement ui/src/components/TodoForm.js then run pytest tests/e2e/ -v

> implement ui/src/components/FilterBar.js then run pytest tests/e2e/ -v

> implement ui/src/components/TodoList.js then run pytest tests/e2e/ -v

> implement ui/index.html then run pytest tests/e2e/ -v
```

Target: **12 passed**.

### Step 5 — refactor

Clean up the code however you like. Keep all 28 tests green.

```bash
pytest tests/ -v               # 28 passed
```

---

## Useful Claude Code slash commands

| Command | When to use |
|---------|-------------|
| `/plan` | Ask Claude to describe its approach before making any changes |
| `/review` | Review the code that was just written |
| `/compact` | Summarise the session context to save tokens on long sessions |
| `/clear` | Start a fresh context window |

---

## Tips

**One layer at a time.** Asking Claude to implement everything at once leads to
cascading errors that are hard to debug. Implement one file, run the tests, repeat.

**End every prompt with `then run pytest`.** This tells Claude whether its
implementation actually worked, so it can self-correct without a second prompt.

**Use `/plan` before large tasks.** Review the plan and confirm before Claude
touches any files.

**Do not modify the tests.** If a test fails, fix the source code — not the test.
The tests are the contract.

---

## Running the finished app

```bash
uvicorn src.main:app --reload
```

- UI  → http://localhost:8000
- API docs → http://localhost:8000/docs
