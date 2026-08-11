from pydantic import BaseModel, ConfigDict, Field


class BookCreate(BaseModel):
    """Validated fields accepted when a new book is created."""

    title: str = Field(min_length=2, max_length=120, examples=["Clean Code"])
    author: str = Field(min_length=2, max_length=80, examples=["Robert C. Martin"])
    category: str = Field(min_length=2, max_length=40, examples=["Software"])


class AvailabilityUpdate(BaseModel):
    """Payload used to change whether a book may be borrowed."""

    available: bool


class Book(BookCreate):
    """Book returned by the API."""

    id: int
    available: bool = True
    model_config = ConfigDict(from_attributes=True)


class BookStats(BaseModel):
    total: int
    available: int
    unavailable: int
    categories: dict[str, int]
