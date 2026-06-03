# Prompt: Implement backend (Green phase)

Read these files first:
- `CLAUDE.md`
- `docs/ARCHITECTURE.md`
- `tests/unit/[relevant_test_file].py`   ← the tests that must pass

Implement **[FEATURE]** to make the tests pass:
1. Write only what is necessary to make the tests pass — do not over-engineer
2. Follow the layer order: Router → Service → Repository
3. Do not modify or skip any existing tests
4. If new dependencies are required, state them explicitly

After implementing, run `pytest tests/unit/ -v` and report the result.
