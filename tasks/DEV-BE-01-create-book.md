# DEV-BE-01 — Create-book endpoint

**Difficulty:** Beginner · **Expected effort:** 2.5 hours

Implement `POST /api/books` using the supplied schema and repository.

## Allowed files

- `app/routes/books.py`
- New `tests/test_create_book.py`

## Acceptance criteria

- Valid payload returns 201 and the created book with generated ID.
- New books default to `available: true`.
- Pydantic returns 422 for missing/short fields.
- Matching title and author, ignoring case and surrounding spaces, returns 409.
- Created book appears in a later GET request.
- Tests cover success, validation and duplicate cases; `pytest -q` passes.
