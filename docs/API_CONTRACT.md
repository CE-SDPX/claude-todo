# API Contract — Todo List API

**Base URL:** `/api/v1`

All request and response bodies use `application/json`.

---

## POST /todos
Create a new todo item.

**Request body**
```json
{ "title": "string (1–200 chars)", "description": "string | null" }
```

**Response 201**
```json
{
  "id": 1,
  "title": "Buy milk",
  "description": null,
  "status": "pending",
  "created_at": "2024-01-01T00:00:00"
}
```

**Errors**
- `422` — validation error (empty title, title too long, etc.)

---

## GET /todos
List todos with optional filters and pagination.

**Query parameters**
| Param    | Default | Description                          |
|----------|---------|--------------------------------------|
| `page`   | `1`     | Page number (≥ 1)                    |
| `size`   | `20`    | Items per page (1–100)               |
| `status` | —       | Filter by `"pending"` or `"done"`    |
| `q`      | —       | Case-insensitive keyword search in title |

**Response 200**
```json
{
  "items": [ { ...todo } ],
  "total": 42,
  "page": 1,
  "size": 20
}
```

---

## GET /todos/{id}
Fetch a single todo by primary key.

**Response 200** — todo object

**Response 404**
```json
{ "detail": { "msg": "Todo not found", "id": 999 } }
```

---

## PATCH /todos/{id}
Partially update a todo. All fields are optional.

**Request body**
```json
{
  "title":       "string (1–200 chars) | null",
  "description": "string | null",
  "status":      "\"pending\" | \"done\" | null"
}
```

**Response 200** — updated todo object

**Response 404** — not found

---

## DELETE /todos/{id}
Delete a todo permanently.

**Response 204** — no content

**Response 404** — not found
