from fastapi import APIRouter, HTTPException, Query, status

from app.models import AvailabilityUpdate, Book, BookCreate
from app.repository import book_repository


router = APIRouter(prefix="/api/books", tags=["Books"])


@router.get("", response_model=list[Book], summary="Browse books")
def list_books(
    search: str | None = Query(default=None, min_length=1),
    category: str | None = Query(default=None, min_length=1),
    available: bool | None = None,
    limit: int = Query(default=20, ge=1, le=50),
    offset: int = Query(default=0, ge=0),
) -> list[Book]:
    """DEV-BE-02 implements filtering and pagination."""
    del search, category, available
    return book_repository.all()[offset : offset + limit]


@router.post("", response_model=Book, status_code=status.HTTP_201_CREATED, summary="Create a book")
def create_book(payload: BookCreate) -> Book:
    """DEV-BE-01 implements duplicate protection and creation."""
    del payload
    raise HTTPException(status_code=501, detail="Complete DEV-BE-01 to create books")


@router.patch("/{book_id}/availability", response_model=Book, summary="Change availability")
def update_availability(book_id: int, payload: AvailabilityUpdate) -> Book:
    """DEV-BE-03 implements availability updates."""
    del book_id, payload
    raise HTTPException(status_code=501, detail="Complete DEV-BE-03 to update availability")


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a book")
def delete_book(book_id: int) -> None:
    """DEV-BE-04 implements deletion and missing-resource behavior."""
    del book_id
    raise HTTPException(status_code=501, detail="Complete DEV-BE-04 to delete books")
