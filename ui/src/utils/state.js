/**
 * Application state — single source of truth for the UI.
 *
 * Rules:
 *   - Components must not store their own state.
 *   - All state changes go through setState().
 *   - Subscribers are notified synchronously after every setState() call.
 *
 * Shape of state:
 *   {
 *     todos:   any[]         — current list of todo objects
 *     filter:  string        — "all" | "pending" | "done"
 *     query:   string        — current keyword search string
 *     loading: boolean       — true while an API call is in flight
 *     error:   string | null — most recent error message, or null
 *   }
 *
 * Functions to implement and export:
 *
 *   getState() → snapshot of current state (plain object, not a reference)
 *
 *   setState(patch) → void
 *     Merge patch into state, then call every registered listener.
 *
 *   subscribe(fn) → unsubscribeFn
 *     Register a listener called with the new state on every change.
 *     Returns a function that removes the listener when called.
 */

// TODO: define the initial state object
// TODO: implement getState, setState, subscribe
