from bs4 import BeautifulSoup

from crowleer.api.schemas import Job, MAX_DESCRIPTION_LENGTH
from crowleer.crawlers.base import PageCrowleer
from crowleer.loader import PageLoader


class WurCrowleer(PageCrowleer):
    url = 'https://www.wur.nl'

    def __init__(self, company_id: int) -> None:
        self.company_id = company_id
        self.loader = PageLoader(timeout=0.1)

    def parse(self) -> list[Job]:
        url = f'{self.url}/en/Jobs/Vacancies.htm'
        content = self.loader.load(url)

        soup = BeautifulSoup(content, features='html.parser')
        job_list = soup.find_all('ul', class_='result-list')[0]
        jobs_items = job_list.find_all('li', class_='result')
        job_links = [job_item.find('a').get('href') for job_item in jobs_items]

        jobs = []
        for link in job_links:
            content = self.loader.load(f'{self.url}{link}')
            job = self.parse_job(content, link)
            jobs.append(job)

        return jobs

    def parse_job(self, content: bytes, link: str) -> Job:
        soup = BeautifulSoup(content, features='html.parser')
        description_header = soup.find('h2', id='We_are_looking_for-anchor')
        description = description_header.find_next_sibling('p').get_text()
        return Job(
            uid=-1,
            name=soup.find('h1', id='content').get_text(),
            url=f'{self.url}{link}',
            description=description[:MAX_DESCRIPTION_LENGTH],
        )
