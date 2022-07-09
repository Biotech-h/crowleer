from bs4 import BeautifulSoup
from dataclasses import dataclass
import httpx
import time


@dataclass
class Job:
    name: str
    href: str
    descr: str

class PageLoader:
    def __init__(self, timeout: int, url: str) -> None:
        self.timeout = timeout
        self.url = url

    def to_html(self, content: bytes, filename: str) -> None:
        with open(filename, "wb") as fs:
            fs.write(content)


    def load(self, url: str) -> bytes:
        time.sleep(self.timeout)
        url = self.url
        resp = httpx.get(url)
        resp.raise_for_status()
        return resp.content

    def read_file(self, filename: str) -> bytes:
        with open(filename, "rb") as fs:
            return fs.read()

class PageCrowleer:
    def __init__(self, url: str):
        self.jobloader = PageLoader(timeout=0.1)
        self.url = url

    def parse(self, content: bytes) -> list[Job]:
        soup = BeautifulSoup(content, features="html.parser")
        job_list = soup.find_all("ul", class_="result-list")[0]
        jobs_items = job_list.find_all("li", class_="result")
        job_links = [job_item.find("a").get("href") for job_item in jobs_items]
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





