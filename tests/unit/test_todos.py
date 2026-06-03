"""Backend unit tests — Red phase.

These tests define the expected behaviour of the API.
Run them before implementing any source code:

    pytest tests/unit/ -v

Every test should FAIL until the corresponding implementation is complete.
Do not modify these tests during the Green phase — fix the source code instead.
"""

import pytest


# ---------------------------------------------------------------------------
# CREATE  POST /api/v1/todos
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_create_todo_valid_title_returns_201_with_id(client):
    """A valid title must return 201 with a non-null id."""
    resp = await client.post("/api/v1/todos", json={"title": "Buy milk"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] is not None
    assert data["title"] == "Buy milk"
    assert data["status"] == "pending"
    assert "created_at" in data


@pytest.mark.asyncio
async def test_create_todo_with_description_persists_description(client):
    """An optional description must be stored and returned."""
    resp = await client.post(
        "/api/v1/todos",
        json={"title": "Buy milk", "description": "2% fat"},
    )
    assert resp.status_code == 201
    assert resp.json()["description"] == "2% fat"


@pytest.mark.asyncio
async def test_create_todo_empty_title_returns_422(client):
    """An empty title string must be rejected with 422."""
    resp = await client.post("/api/v1/todos", json={"title": ""})
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_create_todo_missing_title_returns_422(client):
    """A request body without a title field must return 422."""
    resp = await client.post("/api/v1/todos", json={})
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_create_todo_title_over_200_chars_returns_422(client):
    """A title longer than 200 characters must be rejected with 422."""
    resp = await client.post("/api/v1/todos", json={"title": "x" * 201})
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# READ  GET /api/v1/todos/{id}
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_get_existing_todo_returns_200_with_data(client):
    """Fetching an existing todo by id must return 200 with its data."""
    created = (await client.post("/api/v1/todos", json={"title": "Task"})).json()
    resp = await client.get(f"/api/v1/todos/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["id"] == created["id"]


@pytest.mark.asyncio
async def test_get_nonexistent_todo_returns_404_with_id_in_detail(client):
    """Fetching a todo that does not exist must return 404 with the id in detail."""
    resp = await client.get("/api/v1/todos/999")
    assert resp.status_code == 404
    assert resp.json()["detail"]["id"] == 999


# ---------------------------------------------------------------------------
# LIST  GET /api/v1/todos
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_list_todos_returns_items_and_total(client):
    """Listing todos must return an items array and a total count."""
    await client.post("/api/v1/todos", json={"title": "A"})
    await client.post("/api/v1/todos", json={"title": "B"})
    resp = await client.get("/api/v1/todos")
    assert resp.status_code == 200
    body = resp.json()
    assert body["total"] == 2
    assert len(body["items"]) == 2


@pytest.mark.asyncio
async def test_list_todos_filter_done_excludes_pending_items(client):
    """Filtering by status=done must exclude pending todos."""
    await client.post("/api/v1/todos", json={"title": "Pending task"})
    r = await client.post("/api/v1/todos", json={"title": "Done task"})
    await client.patch(f"/api/v1/todos/{r.json()['id']}", json={"status": "done"})

    resp = await client.get("/api/v1/todos?status=done")
    items = resp.json()["items"]
    assert len(items) == 1
    assert all(t["status"] == "done" for t in items)


@pytest.mark.asyncio
async def test_list_todos_search_q_matches_title_substring(client):
    """Searching with q=milk must return only todos whose title contains 'milk'."""
    await client.post("/api/v1/todos", json={"title": "Buy milk"})
    await client.post("/api/v1/todos", json={"title": "Do laundry"})
    resp = await client.get("/api/v1/todos?q=milk")
    items = resp.json()["items"]
    assert len(items) == 1
    assert "milk" in items[0]["title"].lower()


@pytest.mark.asyncio
async def test_list_todos_pagination_size_limits_items(client):
    """Requesting size=2 must return at most 2 items."""
    for i in range(5):
        await client.post("/api/v1/todos", json={"title": f"Task {i}"})
    resp = await client.get("/api/v1/todos?size=2")
    body = resp.json()
    assert len(body["items"]) == 2
    assert body["total"] == 5


# ---------------------------------------------------------------------------
# UPDATE  PATCH /api/v1/todos/{id}
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_update_todo_status_to_done_returns_updated_status(client):
    """Patching status to done must return the updated status."""
    r = await client.post("/api/v1/todos", json={"title": "Task"})
    todo_id = r.json()["id"]
    resp = await client.patch(f"/api/v1/todos/{todo_id}", json={"status": "done"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "done"


@pytest.mark.asyncio
async def test_update_todo_title_returns_new_title(client):
    """Patching the title must return the new title."""
    r = await client.post("/api/v1/todos", json={"title": "Old title"})
    todo_id = r.json()["id"]
    resp = await client.patch(f"/api/v1/todos/{todo_id}", json={"title": "New title"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "New title"


@pytest.mark.asyncio
async def test_update_nonexistent_todo_returns_404(client):
    """Patching a todo that does not exist must return 404."""
    resp = await client.patch("/api/v1/todos/999", json={"title": "X"})
    assert resp.status_code == 404


# ---------------------------------------------------------------------------
# DELETE  DELETE /api/v1/todos/{id}
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_delete_existing_todo_returns_204(client):
    """Deleting an existing todo must return 204."""
    r = await client.post("/api/v1/todos", json={"title": "To delete"})
    resp = await client.delete(f"/api/v1/todos/{r.json()['id']}")
    assert resp.status_code == 204


@pytest.mark.asyncio
async def test_delete_todo_then_get_returns_404(client):
    """After deletion, fetching the same id must return 404."""
    r = await client.post("/api/v1/todos", json={"title": "To delete"})
    todo_id = r.json()["id"]
    await client.delete(f"/api/v1/todos/{todo_id}")
    assert (await client.get(f"/api/v1/todos/{todo_id}")).status_code == 404


@pytest.mark.asyncio
async def test_delete_nonexistent_todo_returns_404(client):
    """Deleting a todo that does not exist must return 404."""
    resp = await client.delete("/api/v1/todos/999")
    assert resp.status_code == 404
