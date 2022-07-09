import httpx
import orjson

from crowleer.api.schemas import Job


class JobApi:

    def __init__(self, url: str) -> None:
        self.url = url

    def add(self, job: Job) -> Job:
        json_job = orjson.dumps(job.dict())
        headers = {
            'Content-Type': 'application/json',
        }
        respose = httpx.post(f'{self.url}/api/v1/companies/jobs', content=json_job, headers=headers)
        respose.raise_for_status()

        payload = respose.json()
        return Job(**payload)

    def get_by_url(self, company_id: int, url: str) -> Job | None:
        response = httpx.get(f'{self.url}/api/v1/companies/{company_id}/jobs/', params={
            'url': url,
        })

        if response.status_code == httpx.codes.NOT_FOUND:
            return None

        response.raise_for_status()

        job = response.json()
        return Job(**job)
