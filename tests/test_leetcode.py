import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_leetcode_endpoint():
    response = client.get("/leetcode/Priyankar_")
    assert response.status_code in [200, 403]
