# DEV-BE-05 — Catalog statistics endpoint

**Difficulty:** Beginner · **Expected effort:** 3 hours

Implement `GET /api/stats` from the current in-memory catalog.

## Allowed files

- `app/routes/stats.py`
- New `tests/test_stats.py`

## Acceptance criteria

- Response follows the supplied `BookStats` model.
- Total equals available plus unavailable.
- Category counts include every current book and use its category label.
- Values update after create, availability change or deletion.
- Empty catalog returns zeros and an empty categories object.
- Tests cover seeded, mutated and empty catalogs; `pytest -q` passes.
