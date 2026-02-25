import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


POSTS = {
    1: {"userId": 1, "id": 1, "title": "post 1", "body": "body 1"},
    10: {"userId": 1, "id": 10, "title": "post 10", "body": "body 10"},
    100: {"userId": 10, "id": 100, "title": "post 100", "body": "body 100"},
}


class MockApiHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code: int, body: dict) -> None:
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self) -> None:  # noqa: N802
        if self.path.startswith("/posts/"):
            post_id = self.path.split("/")[-1]
            if post_id.isdigit() and int(post_id) in POSTS:
                self._send_json(200, POSTS[int(post_id)])
                return
            self._send_json(404, {})
            return

        self._send_json(404, {})

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/posts":
            self._send_json(404, {})
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
        payload["id"] = 101
        self._send_json(201, payload)

    def log_message(self, format: str, *args: object) -> None:
        return


class MockApiServer:
    def __init__(self) -> None:
        self.httpd = HTTPServer(("127.0.0.1", 0), MockApiHandler)
        self.thread = Thread(target=self.httpd.serve_forever, daemon=True)

    @property
    def base_url(self) -> str:
        host, port = self.httpd.server_address
        return f"http://{host}:{port}"

    def start(self) -> None:
        self.thread.start()

    def stop(self) -> None:
        self.httpd.shutdown()
        self.thread.join(timeout=2)
