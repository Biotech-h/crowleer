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
        client.jobs.add(job)


if __name__ == '__main__':
    main()
