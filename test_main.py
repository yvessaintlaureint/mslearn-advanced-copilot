from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]
    def test_spain_cities():
        response = client.get("/countries/Spain")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0


    def test_monthly_average_spain():
        response = client.get("/countries/Spain/Madrid/January")
        assert response.status_code == 200