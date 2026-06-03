/**
 * TodoForm — form for adding a new todo.
 *
 * Required data-testid attributes (Playwright depends on these):
 *   todo-form    the <form> element
 *   todo-input   the title <input>
 *   add-button   the submit <button>
 *   form-error   the validation error <p> (hidden by default)
 *
 * Behaviour to implement:
 *   - On submit with an empty title: show form-error, do not call the API.
 *   - On submit with a valid title: call api.createTodo, re-fetch the list,
 *     update state, clear the input, and return focus to the input.
 *   - Hide form-error as soon as the user starts typing again.
 *
 * @param {HTMLElement} container - The element to append the form into.
 */

// TODO: implement mountTodoForm(container)
export function mountTodoForm(container) {
  throw new Error("mountTodoForm is not implemented yet");
}
