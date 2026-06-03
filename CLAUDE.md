# Todo List App — AI Context

## Project overview
Full-stack todo list application: FastAPI backend + Vanilla JS frontend.
No JS framework — the backend serves the UI as static files.

## Tech stack

### Backend
- Python 3.11+
- FastAPI 0.110+
- SQLAlchemy 2.0 (async) + aiosqlite
- Pydantic v2
- pytest + httpx (unit tests)
- Playwright + pytest-playwright (e2e tests)

### Frontend
- Vanilla JS with ES Modules (no bundler, no npm)
- HTML5 + CSS3 (CSS custom properties)
- No React / Vue / Angular

## Conventions

### Backend
- Use async/await everywhere possible
- Repository pattern: business logic must NOT live in routers
- Write tests before implementation (TDD — Red → Green → Refactor)
- Always raise HTTPException with a dict detail, e.g. `{"msg": "...", "id": id}`
- Never use `import *`
- Every public function must have a docstring

### Frontend
- All fetch calls must go through `ui/src/api/client.js` only
- A component is a function that creates or updates DOM elements
- Application state lives exclusively in `ui/src/utils/state.js`
- Components must not store their own state
- Every exported function must have a JSDoc comment
- Never use `innerHTML` with user-supplied data — use `textContent` to prevent XSS
- Use CSS class toggles instead of inline styles set via JS

## Constraints
- Never hard-code DATABASE_URL — read it from `src/config.py` settings
- Never return a raw SQLAlchemy model from a route — map it to a Pydantic schema first
- UI data-testid attributes are required on every interactive element (Playwright depends on them)

## Key files
- `docs/PRD.md`          — requirements and acceptance criteria
- `docs/ARCHITECTURE.md` — full-stack component design and data flow
- `docs/API_CONTRACT.md` — endpoint specifications (UI must follow this contract)
- `docs/UI_SPEC.md`      — UI component spec and interaction design
- `docs/adr/`            — architecture decision records
