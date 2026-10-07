from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_info_has_expected_fields():
    body = client.get("/info").json()
    for field in ("hostname", "python_version", "uptime_seconds", "version"):
        assert field in body