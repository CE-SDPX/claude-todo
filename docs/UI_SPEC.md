# UI Spec — Todo List App

## Page structure
Single-page application — no client-side routing.
Everything lives on one screen.

---

## Component specifications

### Header
- Displays the application title
- Shows a live count badge (updates when the todo list changes)
- `data-testid="count-badge"`

### TodoForm
- A text input for the todo title (`data-testid="todo-input"`)
- An Add button (`data-testid="add-button"`)
- An inline error message shown when the title is empty (`data-testid="form-error"`)
- On successful add: clear the input, return focus to the input

### FilterBar
- Three tabs: All, Pending, Done
  - `data-testid="filter-all"`, `"filter-pending"`, `"filter-done"`
- A keyword search input with 300 ms debounce (`data-testid="search-input"`)
- Active tab is visually highlighted

### TodoList
- Container element (`data-testid="todo-list"`)
- Skeleton placeholder shown while loading (`data-testid="skeleton"`)
- Empty state shown when there are no items (`data-testid="empty-state"`)

### TodoItem
- Container element (`data-testid="todo-item"`, `data-id="{id}"`)
- Checkbox to toggle status (`data-testid="todo-checkbox"`)
- Title span (`data-testid="todo-title"`)
- Inline edit input — shown only when editing (`data-testid="todo-edit-input"`)
- Delete button (`data-testid="delete-button"`)

### Toast
- Error notification (`data-testid="toast"`)
- Auto-dismisses after 3 seconds
- `role="alert"` for accessibility

---

## Interactions

### Add todo
1. User types a title in `todo-input`
2. Presses Enter or clicks `add-button`
3. If title is empty → show `form-error`, do not call the API
4. On success → clear input, re-fetch list, scroll to new item

### Toggle status
1. User clicks `todo-checkbox`
2. UI updates immediately (optimistic)
3. PATCH request sent in background
4. On error → revert checkbox, show toast

### Inline edit
1. User double-clicks `todo-title`
2. Replace span with `todo-edit-input` pre-filled with current title
3. Pressing Enter → PATCH new title, replace input with updated span
4. Pressing Escape → cancel, restore original span
5. Blur (click away) → same as Enter

### Delete
1. User clicks `delete-button`
2. Item fades out optimistically
3. DELETE request sent
4. On error → restore item, show toast

### Filter / Search
1. Click a filter tab → re-fetch with `?status=` param
2. Type in search input → debounce 300 ms → re-fetch with `?q=` param
3. Filter and search can be combined

---

## Loading and error states

| State     | What the user sees                          |
|-----------|---------------------------------------------|
| `loading` | 3 skeleton card placeholders                |
| `empty`   | "No todos yet" message in the list area     |
| `error`   | Toast notification, auto-dismissed after 3 s|

---

## Acceptance criteria (UI)
| ID        | Criterion |
|-----------|-----------|
| AC-UI-01  | Adding a todo shows it in the list immediately |
| AC-UI-02  | Toggling checkbox updates the visual state immediately |
| AC-UI-03  | Deleting a todo removes it from the list |
| AC-UI-04  | Filter "Done" shows only done items |
| AC-UI-05  | Searching by keyword filters the list |
| AC-UI-06  | Empty title + Add → error message shown, no API request sent |
| AC-UI-07  | Failing API call → toast error notification shown |
