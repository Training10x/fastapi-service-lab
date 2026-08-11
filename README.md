# FastAPI Service Lab

A small, professional API starter for five independent Training10x backend assignments. It uses a resettable in-memory repository, so students do not need PostgreSQL, Docker, accounts, environment variables or API keys.

## Quick start

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

macOS/Linux activation: `source .venv/bin/activate`.

Open:

- API documentation: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

Run checks with `pytest -q`. Read [START_HERE.md](START_HERE.md) before the assigned task.

| ID | Task | Expected effort |
|---|---|---:|
| DEV-BE-01 | Create-book endpoint | 2.5 hours |
| DEV-BE-02 | Search, filters and pagination | 3 hours |
| DEV-BE-03 | Availability update endpoint | 2 hours |
| DEV-BE-04 | Delete-book endpoint | 2 hours |
| DEV-BE-05 | Catalog statistics endpoint | 3 hours |
