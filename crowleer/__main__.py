import logging

from crowleer.api.client import client
from crowleer.api.schemas import Job
from crowleer.config import config
from crowleer.crawlers.base import PageCrowleer
from crowleer.crawlers.wur import WurCrowleer

logger = logging.getLogger(__name__)

crawlers: list[PageCrowleer] = [
    WurCrowleer(config.companies['wur']),
]


def main():
    logging.basicConfig(level=config.loglevel)
    for crawler in crawlers:
        jobs = crawler.parse()
        add_jobs(crawler.company_id, jobs)


def add_jobs(company_id: int, jobs: list[Job]) -> None:
    for job in jobs:
        logger.debug(job)
        job_found = client.jobs.get_by_url(company_id, job.url)
        if job_found:
            continue

        client.jobs.add(job)


if __name__ == '__main__':
    main()
