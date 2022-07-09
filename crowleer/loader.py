import time

import httpx


class PageLoader:

    def __init__(self, timeout: float) -> None:
        self.timeout = timeout

    def load(self, url: str) -> bytes:
        time.sleep(self.timeout)
        resp = httpx.get(url)
        resp.raise_for_status()
        return resp.content

    def to_html(self, content: bytes, filename: str) -> None:
        with open(filename, 'wb') as fs:
            fs.write(content)

    def read_file(self, filename: str) -> bytes:
        with open(filename, 'rb') as fs:
            return fs.read()
