"""Shared pytest fixtures.

Fixtures:
  db_session  — in-memory SQLite session; schema created and dropped per test
  client      — httpx.AsyncClient wired to the test database via dependency override
"""

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# NOTE: these imports will fail until src/models and src/main are implemented
from src.database import get_session
from src.main import app
from src.models.todo import Base

TEST_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture
async def db_session():
    """Provide an isolated in-memory SQLite session for a single test.

    Creates the full schema before the test and drops it after,
    so every test starts with a clean database.
    """
    engine = create_async_engine(TEST_DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False)
    async with factory() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture
async def client(db_session: AsyncSession):
    """Provide an httpx.AsyncClient that uses the in-memory test database.

    Overrides the get_session FastAPI dependency so that all requests
    in a test share the same isolated session.
    """
    async def override_get_session():
        yield db_session

    app.dependency_overrides[get_session] = override_get_session

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as c:
        yield c

    app.dependency_overrides.clear()
