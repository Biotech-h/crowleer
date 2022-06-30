import orjson
import requests

from crowleer.config import config
from crowleer.api.schemas import Company


class CompanyApi:

    def add(self, company: Company) -> Company:
        json_company = orjson.dumps(company.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = requests.post(f'{config.app_host}:{config.app_port}/api/v1/company/', content=json_company, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return Company(**payload)
