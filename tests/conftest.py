import pytest

from client import ApiClient
from mock_server import MockApiServer


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    server = MockApiServer()
    server.start()

    client = ApiClient(base_url=server.base_url)
    yield client

    server.stop()
