from crowleer.page import PageLoader, PageCrowleer
from crowleer.api.client import client


def main():
    crowleer = PageCrowleer()
    loader = PageLoader()
    # content = loader.load(page=1)
    # loader.to_html(content, "jobs_page.html")
    content = loader.read_file("jobs_page.html")
    jobs = crowleer.parse(content)
    for job in jobs:
        job_unique = client.jobs.check_by_url(job, job['href'])
        client.jobs.add(job_unique)


if __name__ == '__main__':
    main()
