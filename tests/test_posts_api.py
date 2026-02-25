import pytest

from client import ApiClient


def test_get_existing_post_returns_200_and_expected_schema(api_client: ApiClient) -> None:
    response = api_client.get("/posts/1")

    assert response.status_code == 200
    body = response.json()
    assert set(body.keys()) == {"userId", "id", "title", "body"}
    assert body["id"] == 1


@pytest.mark.parametrize("post_id", [1, 10, 100])
def test_get_multiple_existing_posts(api_client: ApiClient, post_id: int) -> None:
    response = api_client.get(f"/posts/{post_id}")

    assert response.status_code == 200
    assert response.json()["id"] == post_id


def test_get_non_existing_post_returns_404(api_client: ApiClient) -> None:
    response = api_client.get("/posts/999999")

    assert response.status_code == 404


def test_create_post_returns_201_and_payload_fields(api_client: ApiClient) -> None:
    payload = {
        "title": "qa title",
        "body": "qa body",
        "userId": 1,
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]
    assert "id" in body
