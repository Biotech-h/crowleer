import orjson
import httpx

from crowleer.api.schemas import Job


class JobApi:
    def __init__(self, url: str) -> None:
        self.url = url

    def add(self, job: Job) -> Job:
        json_job = orjson.dumps(job.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = httpx.post(f'{self.url}/api/v1/company/jobs', content=json_job, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return Job(**payload)

    def check_by_url(self, job: Job, url: Job.url) -> Job:
        response = httpx.get(f'{self.url}/api/v1/company/jobs')
        response.raise_for_status()
        for job_in_base in response.json():
            if url != job_in_base['url']:
                return job
