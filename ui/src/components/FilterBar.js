/**
 * FilterBar — status filter tabs and keyword search input.
 *
 * Required data-testid attributes:
 *   filter-bar      the container element
 *   filter-all      the All tab button
 *   filter-pending  the Pending tab button
 *   filter-done     the Done tab button
 *   search-input    the keyword search <input>
 *
 * Behaviour to implement:
 *   - Clicking a tab: update state.filter, re-fetch todos, mark tab as active.
 *   - Typing in search: debounce 300 ms, update state.query, re-fetch todos.
 *   - Filter and search are combined in the same API call.
 *
 * @param {HTMLElement} container
 */

// TODO: implement mountFilterBar(container)
export function mountFilterBar(container) {
  throw new Error("mountFilterBar is not implemented yet");
}
