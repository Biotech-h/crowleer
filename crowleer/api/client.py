from crowleer.api.companies import CompanyApi
from crowleer.api.jobs import JobApi

class ApiClient:
    def __init__(self) -> None:
        self.jobs = JobApi()
        self.companies = CompanyApi()

client = ApiClient()
