import orjson
from flask import request

from crowleer.api.schemas import CompanyModel


class CompanyApi:

    def add(self, company: CompanyModel) -> CompanyModel:
        json_company = orjson.dumps(company.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = request.post('/api/v1/jobs/', content=json_company, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return CompanyModel(**payload)

client_company = CompanyApi()
