from fastapi import APIRouter, HTTPException

from app.models import BookStats


router = APIRouter(prefix="/api/stats", tags=["Statistics"])


@router.get("", response_model=BookStats, summary="Get catalog statistics")
def get_stats() -> BookStats:
    """DEV-BE-05 implements aggregate catalog statistics."""
    raise HTTPException(status_code=501, detail="Complete DEV-BE-05 to return statistics")
