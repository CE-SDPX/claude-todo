# ADR-002: Vanilla JS instead of React / Vue

## Status
Accepted

## Context
The UI is simple (one screen, CRUD interactions).
A build step adds complexity without meaningful benefit at this scope.

## Decision
Use Vanilla JS with ES Modules — no bundler, no npm, no framework.
FastAPI serves the HTML and JS files directly as static assets.

## Consequences
- ✅ No build step — edit a file, refresh the browser
- ✅ No Node.js dependency
- ✅ Playwright e2e tests exercise the real browser behaviour
- ❌ Manual DOM management becomes verbose as the UI grows
- ❌ Migration to a framework would be needed for a more complex UI
  → The component-function pattern in use makes a future migration manageable
