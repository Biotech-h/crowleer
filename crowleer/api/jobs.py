import orjson
from flask import request

from crowleer.api.schemas import JobModel


class JobApi:

    def add(self, job: JobModel) -> JobModel:
        json_job = orjson.dumps(job.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = request.post('/api/v1/company/jobs', content=json_job, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return JobModel(**payload)

client_job = JobApi()
