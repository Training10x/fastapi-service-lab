# DEV-BE-03 — Availability update endpoint

**Difficulty:** Beginner · **Expected effort:** 2 hours

Implement `PATCH /api/books/{book_id}/availability`.

## Allowed files

- `app/routes/books.py`
- New `tests/test_availability.py`

## Acceptance criteria

- Existing book returns 200 with updated availability.
- Both true and false values work.
- Missing book returns 404 with `Book not found`.
- Invalid or missing boolean returns 422.
- Follow-up GET reflects the update.
- Tests cover all paths; `pytest -q` passes.
