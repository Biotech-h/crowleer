import orjson
import httpx

from crowleer.api.schemas import Company


class CompanyApi:
    def __init__(self, url: str) -> None:
        self.url = url

    def add(self, company: Company) -> Company:
        json_company = orjson.dumps(company.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = httpx.post(f'{self.url}/api/v1/company/', content=json_company, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return Company(**payload)
