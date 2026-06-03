"""Business logic for todo operations.

Rules:
  - Accept a TodoRepository in __init__ and store it as self.repo
  - Raise HTTPException (not DB errors) for not-found and validation failures
  - Map ORM models to Pydantic response schemas before returning
  - Never access the database directly — always go through self.repo

Methods to implement:

  create_todo(data: TodoCreate) -> TodoResponse
    Call repo.create, return TodoResponse.

  get_todo(todo_id: int) -> TodoResponse
    Call repo.get_by_id; raise HTTP 404 if None.

  list_todos(page, size, status, q) -> TodoListResponse
    Call repo.list_todos, wrap result in TodoListResponse.

  update_todo(todo_id, data: TodoUpdate) -> TodoResponse
    Fetch todo (404 if missing), call repo.update with non-None fields.

  delete_todo(todo_id: int) -> None
    Fetch todo (404 if missing), call repo.delete.
"""

# TODO: implement TodoService with all methods above
