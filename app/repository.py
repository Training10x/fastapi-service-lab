from copy import deepcopy

from app.models import Book, BookCreate


SEED_BOOKS = [
    Book(id=1, title="The Pragmatic Programmer", author="Andrew Hunt", category="Software"),
    Book(id=2, title="Designing Data-Intensive Applications", author="Martin Kleppmann", category="Data"),
    Book(id=3, title="Refactoring", author="Martin Fowler", category="Software", available=False),
]


class BookRepository:
    """Small in-memory store. Data resets whenever the process restarts."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._books = deepcopy(SEED_BOOKS)
        self._next_id = max(book.id for book in self._books) + 1

    def all(self) -> list[Book]:
        return deepcopy(self._books)

    def get(self, book_id: int) -> Book | None:
        return next((deepcopy(book) for book in self._books if book.id == book_id), None)

    def create(self, payload: BookCreate) -> Book:
        book = Book(id=self._next_id, **payload.model_dump())
        self._next_id += 1
        self._books.append(book)
        return deepcopy(book)

    def set_availability(self, book_id: int, available: bool) -> Book | None:
        for book in self._books:
            if book.id == book_id:
                book.available = available
                return deepcopy(book)
        return None

    def delete(self, book_id: int) -> bool:
        original_length = len(self._books)
        self._books = [book for book in self._books if book.id != book_id]
        return len(self._books) < original_length


book_repository = BookRepository()
