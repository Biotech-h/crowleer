from abc import ABC, abstractmethod

from crowleer.api.schemas import Job


class Crowleer(ABC):
    company_id: int

    @abstractmethod
    def parse(self) -> list[Job]:
        raise NotImplementedError
