import pytest
from fastapi.testclient import TestClient
#from httpx import AsyncClient
import sys
sys.path.insert(0, "/Users/charles/github/online_diary")
from src.API.api import app


client = TestClient(app)

#we test if the API works and the get operation send the good result
def test_read_text(create_db):
    response = client.get(
        "/text",
        json={"text_date": "2015-08-03"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == [["bonne journée"]]
