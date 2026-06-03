/**
 * API client — the single point of contact between the UI and the backend.
 *
 * Rules:
 *   - All fetch calls must go through this module.
 *   - Errors are normalised to { status, message } and re-thrown.
 *   - A 204 No Content response returns null (no JSON parsing).
 *
 * Functions to implement:
 *
 *   listTodos({ page?, size?, status?, q? }) → Promise<TodoListResponse>
 *     GET /api/v1/todos with the provided query parameters.
 *
 *   createTodo({ title, description? }) → Promise<TodoResponse>
 *     POST /api/v1/todos
 *
 *   updateTodo(id, { title?, description?, status? }) → Promise<TodoResponse>
 *     PATCH /api/v1/todos/{id}
 *
 *   deleteTodo(id) → Promise<null>
 *     DELETE /api/v1/todos/{id}
 */

// TODO: implement a private request(path, options) helper
// TODO: implement and export listTodos, createTodo, updateTodo, deleteTodo
