from fastapi.testclient import TestClient
from home_automation_api.main import app

client = TestClient(app)


def test_light_on():

    response = client.post("/light/on")

    assert response.status_code == 200


def test_light_off():

    response = client.post("/light/off")

    assert response.status_code == 200