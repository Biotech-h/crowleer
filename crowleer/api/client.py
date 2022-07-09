from crowleer.api.jobs import JobApi
from crowleer.config import config


class ApiClient:
    def __init__(self) -> None:
        self.jobs = JobApi(url=config.url)


client = ApiClient()
