
from bs4 import BeautifulSoup
from dataclasses import dataclass
import httpx
import time


@dataclass
class Job:
    name: str
    href: str
    descr: str

class JobLoader:
    url = "https://www.wur.nl"

    def __init__(self, timeout: int) -> None:
        self.timeout = timeout


    def to_html(self, content: bytes, filename: str) -> None:
        with open(filename, "wb") as fs:
            fs.write(content)


    def load(self, link: str) -> bytes:
        time.sleep(self.timeout)
        url = f"{self.url}{link}"
        resp = httpx.get(url)
        resp.raise_for_status()
        return resp.content

    def read_file(self, filename: str) -> bytes:
        with open(filename, "rb") as fs:
            return fs.read()

class PageCrowleer:
    url = "https://www.wur.nl"

    def __init__(self):
        self.jobloader = JobLoader(timeout=0.1)

    def parse(self, content: bytes) -> list[Job]:
        soup = BeautifulSoup(content, features="html.parser")
        job_list = soup.find_all("ul", class_="result-list")[0]
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



class PageLoader:
    url = "https://www.wur.nl/en/Jobs/Vacancies.htm"

    def to_html(self, content: bytes, filename: str) -> None:
        with open(filename, "wb") as fs:
            fs.write(content)


    def load(self, page: int) -> bytes:
        url = self.url
        resp = httpx.get(url, params={"from": str(page * 10)})
        resp.raise_for_status()
        return resp.content

    def read_file(self, filename: str) -> bytes:
        with open(filename, "rb") as fs:
            return fs.read()



# class JobParser:
#     def parse(self, content: bytes) -> JobDetail:
#         return JobDetail()


