"""SQLAlchemy ORM model for the todos table.

Schema (from docs/ARCHITECTURE.md):
  id          INTEGER   Primary key, autoincrement
  title       TEXT      Not null
  description TEXT      Nullable
  status      TEXT      "pending" | "done"   (default: "pending")
  created_at  DATETIME  Server-side default (now)
  updated_at  DATETIME  Auto-updated on every write
"""

# TODO: define DeclarativeBase subclass called Base
# TODO: define Todo(Base) with all columns listed above
#   Use SQLAlchemy 2.0 mapped_column / Mapped syntax
