"""Pydantic v2 schemas for request validation and response serialisation.

Schemas to implement (see docs/API_CONTRACT.md for field details):

  TodoCreate
    - title:       str   required, min_length=1, max_length=200
    - description: str | None   optional

  TodoUpdate   (all fields optional — PATCH semantics)
    - title:       str | None
    - description: str | None
    - status:      Literal["pending", "done"] | None

  TodoResponse  (maps from ORM model — enable from_attributes)
    - id:          int
    - title:       str
    - description: str | None
    - status:      str
    - created_at:  datetime

  TodoListResponse  (paginated list)
    - items:  list[TodoResponse]
    - total:  int
    - page:   int
    - size:   int
"""

# TODO: implement all four schemas above using pydantic.BaseModel
