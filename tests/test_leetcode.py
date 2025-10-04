from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_leetcode_endpoint():
    response = client.get("/leetcode/Priyankar_")
    # Check that the endpoint returns a JSON
    assert response.status_code == 200 or response.status_code == 403
    assert "rank" in response.json() or "error" in response.json()
