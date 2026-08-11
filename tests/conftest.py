import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.repository import book_repository


@pytest.fixture(autouse=True)
def reset_repository():
    book_repository.reset()
    yield
    book_repository.reset()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
