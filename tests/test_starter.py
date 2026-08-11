def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "library-lab"}


def test_seeded_catalog_is_available(client):
    response = client.get("/api/books")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_openapi_lists_all_student_endpoints(client):
    paths = client.get("/openapi.json").json()["paths"]
    assert "/api/books" in paths
    assert "/api/books/{book_id}/availability" in paths
    assert "/api/books/{book_id}" in paths
    assert "/api/stats" in paths
