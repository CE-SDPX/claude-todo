"""FastAPI application entry point.

Responsibilities:
  - Create the FastAPI app instance
  - Register the lifespan handler (calls init_db on startup)
  - Mount the /api/v1 router
  - Serve the UI: mount StaticFiles at /ui and return index.html at GET /
"""

# TODO: implement lifespan context manager that calls init_db()
# TODO: create app = FastAPI(title=settings.app_name, lifespan=lifespan)
# TODO: app.include_router(router)
# TODO: mount StaticFiles(directory="ui") at path "/ui"
# TODO: add GET "/" route that returns FileResponse("ui/index.html")
