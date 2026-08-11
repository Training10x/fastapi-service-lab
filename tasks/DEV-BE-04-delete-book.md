# DEV-BE-04 — Delete-book endpoint

**Difficulty:** Beginner · **Expected effort:** 2 hours

Implement `DELETE /api/books/{book_id}` using the repository.

## Allowed files

- `app/routes/books.py`
- New `tests/test_delete_book.py`

## Acceptance criteria

- Existing book returns 204 with an empty body.
- Deleted book no longer appears in the list.
- Deleting an unknown or already-deleted ID returns 404 with `Book not found`.
- Other books remain unchanged.
- Tests cover success and missing cases; `pytest -q` passes.
