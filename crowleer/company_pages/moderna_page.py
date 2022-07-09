from bs4 import BeautifulSoup
from dataclasses import dataclass
import httpx
import time
from crowleer.company_pages.base import Job, PageLoader, PageCrowleer, PageLoader


class ModernaLoader(PageLoader):
    def __init__(self, timeout=0.1, url="https://modernatx.wd1.myworkdayjobs.com/M_tx") -> None:
        self.timeout = timeout
        self.url = url


class ModernaCrowleer(PageCrowleer):
    def __init__(self, url="https://modernatx.wd1.myworkdayjobs.com/M_tx"):
        self.jobloader = ModernaLoader()
        self.url = url

    def parse(self, content: bytes) -> list[Job]:
        soup = BeautifulSoup(content, features="html.parser")
        job_list = soup.find_all("div", class_='WNLO WBLO')
        for job in job_list:
            name = job.find("div", class_="gwt-Label W050 WH40").text
        jobs_items = job_list.find_all("li", class_="result")
        job_links = [job_item.find("a").get("href") for job_item in jobs_items]
        # content = self.jobloader.load(job_links[0])
        # self.jobloader.to_html(content, "job.html")
        jobs = []
        for link in job_links:
            content = self.jobloader.read_file("job.html")
            job = self.parse_job(content, link)
            jobs.append(job)

        return jobs



    def parse_job(self, content: bytes, link: str) -> Job:
        soup = BeautifulSoup(content, features="html.parser")
        return Job(
            name=soup.find("h1", id="content").get_text(),
            href=f"{self.url}{link}",
            descr=soup.find("h2", id="We_are_looking_for-anchor").find_next_sibling("p").get_text(),
        )

