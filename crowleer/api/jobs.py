import orjson
import requests

from crowleer.config import config
from crowleer.api.schemas import Job


class JobApi:

    def add(self, job: Job) -> Job:
        json_job = orjson.dumps(job.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = requests.post(f'{config.app_host}:{config.app_port}/api/v1/company/jobs', content=json_job, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return Job(**payload)
