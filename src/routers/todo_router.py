"""FastAPI router for /api/v1/todos.

Rules:
  - HTTP concerns only — no business logic
  - Validate input with Pydantic schemas
  - Delegate all work to TodoService
  - Use Depends(get_service) to receive a ready-made service instance

Endpoints to implement (see docs/API_CONTRACT.md for full specs):

  POST   /api/v1/todos            → status 201, response TodoResponse
  GET    /api/v1/todos            → status 200, response TodoListResponse
                                    query params: page, size, status, q
  GET    /api/v1/todos/{todo_id}  → status 200, response TodoResponse
  PATCH  /api/v1/todos/{todo_id}  → status 200, response TodoResponse
  DELETE /api/v1/todos/{todo_id}  → status 204, no body

Dependency get_service(session):
  Build and return TodoService(TodoRepository(session))
"""

# TODO: define router = APIRouter(prefix="/api/v1/todos", tags=["todos"])
# TODO: implement get_service dependency
# TODO: implement all five route handlers above
