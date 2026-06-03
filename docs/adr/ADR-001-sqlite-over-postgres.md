# ADR-001: SQLite instead of PostgreSQL

## Status
Accepted

## Context
This project is small-scale and does not require high concurrent write throughput.
A simpler deployment story (no separate DB server) is preferred.

## Decision
Use SQLite with the `aiosqlite` async driver.

## Consequences
- ✅ Zero-config — no database server to install or manage
- ✅ Tests run with an in-memory SQLite database (fast and isolated)
- ✅ Single file to back up
- ❌ Not suitable for high-concurrency production workloads
- ❌ Migration to PostgreSQL would be needed if the app scales
  → The repository pattern means only `DATABASE_URL` and the driver need to change
