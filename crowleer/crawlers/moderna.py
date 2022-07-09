from glom import glom

from crowleer.api.schemas import Job
from crowleer.crawlers.base import Crowleer
from crowleer.loader import PageLoader


class ModernaCrowleer(Crowleer):
    url = 'https://modernatx.wd1.myworkdayjobs.com'

    def __init__(self, company_id: int) -> None:
        self.loader = PageLoader(timeout=0.1)
        self.company_id = company_id

    def parse(self) -> list[Job]:
        data = self.loader.load_json(f'{self.url}/M_tx')
        data = data['body']['children'][0]['children'][0]
        job_titles = glom(data, ('listItems', ['title']))

        jobs = []
        for job_title in job_titles:
            command_link = job_title['commandLink']
            job = Job(
                uid=-1,
                name=job_title['instances'][0]['text'],
                url=f'{self.url}{command_link}',
                company_uid=self.company_id,
            )
            jobs.append(job)

        return jobs
