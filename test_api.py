import requests
import pytest

def test_api():
    response = requests.get("https://google.com")
    assert response.status_code == 200