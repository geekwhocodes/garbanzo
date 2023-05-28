

from httpx import Response


def test_health(test_app):
    response : Response = test_app.get("/health")

    assert response.status_code == 200
    assert response.json() == True
