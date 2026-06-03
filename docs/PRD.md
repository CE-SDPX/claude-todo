# PRD — Todo List App

## Goal
A full-stack todo application with a FastAPI JSON API and a Vanilla JS single-page UI.

---

## User stories

### API
- US-01: Create a todo with a title and an optional description
- US-02: List all todos with pagination
- US-03: Get a single todo by id
- US-04: Update a todo's title, description, or status
- US-05: Delete a todo
- US-06: Filter todos by status (pending / done)
- US-07: Search todos by keyword in title

### UI
- US-08: See the full todo list immediately on page load
- US-09: Add a new todo through an input form
- US-10: Toggle a todo's status between pending and done via a checkbox
- US-11: Edit a todo title inline by double-clicking it
- US-12: Delete a todo with a delete button
- US-13: Filter todos using All / Pending / Done tabs
- US-14: Search todos with a keyword search input
- US-15: See a skeleton loading state while data is fetching
- US-16: See an error toast notification when an API call fails

---

## Acceptance criteria

### Backend
| ID     | Criterion |
|--------|-----------|
| AC-01  | `title` must not be empty; length 1–200 chars |
| AC-02  | `status` defaults to `"pending"` on creation |
| AC-03  | Response must include `id` and `created_at` |
| AC-04  | Pagination defaults: `page=1`, `size=20`; `size` max 100 |
| AC-05  | Only `"pending"` and `"done"` are valid status values |

### UI
| ID        | Criterion |
|-----------|-----------|
| AC-UI-01  | Adding a todo shows it in the list immediately |
| AC-UI-02  | Toggling a checkbox updates the visual state immediately |
| AC-UI-03  | Deleting a todo removes it from the list |
| AC-UI-04  | Filter "Done" shows only done items |
| AC-UI-05  | Searching by keyword filters the list |
| AC-UI-06  | Submitting an empty title shows a UI error and does not send a request |
| AC-UI-07  | A failing API call shows an error toast notification |
