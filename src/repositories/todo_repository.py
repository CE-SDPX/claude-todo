"""Database operations for the todos table.

Rules:
  - Zero business logic here — only SQL / ORM queries
  - Accept an AsyncSession in __init__ and store it as self.session
  - Return raw SQLAlchemy model instances (not Pydantic schemas)

Methods to implement:

  create(title, description) -> Todo
    Insert a new row and return the refreshed instance.

  get_by_id(todo_id) -> Todo | None
    SELECT by primary key; return None if not found.

  list_todos(page, size, status, q) -> tuple[list[Todo], int]
    Return (items, total_count).
    - Filter by status when provided.
    - Filter by title ILIKE %q% when q is provided.
    - Apply OFFSET / LIMIT for pagination.

  update(todo, **fields) -> Todo
    Set each field whose value is not None, commit, refresh, return.

  delete(todo) -> None
    Delete the row and commit.
"""

# TODO: implement TodoRepository with all methods above
