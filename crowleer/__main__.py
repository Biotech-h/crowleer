import logging
import time

import httpx

from crowleer.api.client import client
from crowleer.api.schemas import Job
from crowleer.config import config
from crowleer.crawlers.base import Crowleer
from crowleer.crawlers.moderna import ModernaCrowleer
from crowleer.crawlers.wur import WurCrowleer

logger = logging.getLogger(__name__)

crawlers: list[Crowleer] = [
    WurCrowleer(config.companies['wur']),
    ModernaCrowleer(config.companies['moderna']),
]

HOUR = 3600


def main():
    logging.basicConfig(level=config.loglevel)

    while True:  # noqa: WPS457
        for crawler in crawlers:
            jobs = crawler.parse()
            add_jobs(crawler.company_id, jobs)

        time.sleep(HOUR)

        check_jobs()

        time.sleep(HOUR)


def add_jobs(company_id: int, jobs: list[Job]) -> None:
    for job in jobs:
        logger.debug(job)
        job_found = client.jobs.get_by_url(company_id, job.url)
        if job_found:
            continue

        client.jobs.add(job)


def check_jobs():
    jobs = client.jobs.get_all()
    for job in jobs:
        logger.debug(job)
        response = httpx.get(job.url)

        if response.status_code != 200:
            client.jobs.delete_job(job.uid)


if __name__ == '__main__':
    main()
