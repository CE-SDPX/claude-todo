"""Async SQLAlchemy engine, session factory, and FastAPI dependency."""

# TODO: create an async engine using settings.database_url
# TODO: create an async_sessionmaker bound to the engine
# TODO: implement init_db() — creates all tables on app startup
# TODO: implement get_session() — async generator used as a FastAPI dependency
#   Each request receives a fresh AsyncSession; the session is closed on exit.
