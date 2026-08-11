from fastapi import FastAPI

from app.routes.books import router as books_router
from app.routes.stats import router as stats_router


app = FastAPI(
    title="Training10x Library Service Lab",
    version="1.0.0",
    description="A local, in-memory FastAPI starter for focused student tasks.",
)
app.include_router(books_router)
app.include_router(stats_router)


@app.get("/health", tags=["System"], summary="Check service health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "library-lab"}
