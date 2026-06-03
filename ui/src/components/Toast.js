/**
 * Toast — error notification that auto-dismisses after 3 seconds.
 *
 * Required data-testid attributes:
 *   toast   the notification container (role="alert", aria-live="polite")
 *
 * Behaviour to implement:
 *   - Subscribe to state.error.
 *   - When error is non-null: show the toast with the error message.
 *   - After 3 seconds: hide the toast and call setState({ error: null }).
 *   - Reset the 3-second timer on each new error.
 *
 * @param {HTMLElement} container - Typically document.body.
 */

// TODO: implement mountToast(container)
export function mountToast(container) {
  throw new Error("mountToast is not implemented yet");
}
