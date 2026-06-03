/**
 * TodoList — renders the list of todos and re-renders on state changes.
 *
 * Required data-testid attributes:
 *   todo-list       the <ul> element
 *   skeleton        the loading placeholder (3 skeleton cards)
 *   empty-state     shown when state.todos is empty and not loading
 *   todo-item       each <li> (also needs data-id="{id}")
 *   todo-checkbox   the status toggle checkbox inside each item
 *   todo-title      the title <span> inside each item
 *   todo-edit-input the inline edit <input> (shown only during editing)
 *   delete-button   the delete <button> inside each item
 *
 * Behaviour to implement:
 *   - Subscribe to state changes and re-render when todos / loading changes.
 *   - Show skeleton when state.loading is true.
 *   - Show empty-state when todos is empty and loading is false.
 *   - Checkbox change → optimistic update → PATCH → re-fetch (rollback on error).
 *   - Double-click on todo-title → replace with todo-edit-input.
 *     Enter → save (PATCH), Escape → cancel (restore original span).
 *   - Delete button click → optimistic removal → DELETE → re-fetch (rollback on error).
 *   - Never use innerHTML with user-supplied text — use textContent.
 *
 * @param {HTMLElement} container
 */

// TODO: implement mountTodoList(container)
export function mountTodoList(container) {
  throw new Error("mountTodoList is not implemented yet");
}
