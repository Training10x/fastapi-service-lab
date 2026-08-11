# DEV-BE-02 — Search, filters and pagination

**Difficulty:** Beginner · **Expected effort:** 3 hours

Complete the query behavior of `GET /api/books`.

## Allowed files

- `app/routes/books.py`
- New `tests/test_list_books.py`

## Acceptance criteria

- `search` matches title or author case-insensitively.
- `category` uses a case-insensitive exact match.
- `available` filters boolean availability.
- Filters combine correctly before offset/limit pagination.
- Invalid limit/offset returns 422 through existing validation.
- Tests cover each filter, combined filters and pagination; `pytest -q` passes.
