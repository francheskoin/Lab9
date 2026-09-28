import os
import requests

BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")


def test_get_post():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "title" in data


def test_get_all_posts():
    r = requests.get(f"{BASE_URL}/posts", timeout=10)
    assert r.status_code == 200
    assert len(r.json()) > 0


def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    assert r.status_code == 201
    assert r.json()["title"] == "foo"