from abc import ABC, abstractmethod

from crowleer.api.schemas import Job


class PageCrowleer(ABC):
    company_id: int

    @abstractmethod
    def parse(self) -> list[Job]:
        raise NotImplementedError
