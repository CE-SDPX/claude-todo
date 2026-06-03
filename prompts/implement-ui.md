# Prompt: Implement UI component (Green phase)

Read these files first:
- `CLAUDE.md`
- `docs/ARCHITECTURE.md`
- `docs/UI_SPEC.md`
- `tests/e2e/test_ui_todos.py`   ← the e2e tests that must pass

Implement **[COMPONENT]** to make the e2e tests pass:
1. Add all required `data-testid` attributes (Playwright depends on them)
2. Follow the component tree in `ARCHITECTURE.md`
3. Application state must live in `ui/src/utils/state.js` only
4. All API calls must go through `ui/src/api/client.js` only
5. Never use `innerHTML` with user input — use `textContent`
6. Add a JSDoc comment to every exported function

After implementing, run `pytest tests/e2e/ -v` and report the result.
