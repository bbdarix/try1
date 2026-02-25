import json
import os
from dataclasses import dataclass
from typing import Any
from urllib import error, request


@dataclass
class ApiResponse:
    status_code: int
    _body: bytes

    def json(self) -> dict[str, Any]:
        if not self._body:
            return {}
        return json.loads(self._body.decode("utf-8"))


class ApiClient:
    """Мини-клиент для взаимодействия с REST API без внешних зависимостей."""

    def __init__(self, base_url: str | None = None) -> None:
        self.base_url = (base_url or os.getenv("BASE_URL") or "https://jsonplaceholder.typicode.com").rstrip("/")

    def _request(self, method: str, path: str, json_payload: dict[str, Any] | None = None) -> ApiResponse:
        data = None
        headers: dict[str, str] = {}

        if json_payload is not None:
            data = json.dumps(json_payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = request.Request(
            f"{self.base_url}/{path.lstrip('/')}",
            data=data,
            headers=headers,
            method=method,
        )

        try:
            with request.urlopen(req, timeout=10) as response:
                return ApiResponse(status_code=response.getcode(), _body=response.read())
        except error.HTTPError as exc:
            return ApiResponse(status_code=exc.code, _body=exc.read())

    def get(self, path: str) -> ApiResponse:
        return self._request("GET", path)

    def post(self, path: str, json: dict[str, Any]) -> ApiResponse:
        return self._request("POST", path, json_payload=json)
