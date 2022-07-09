import os
from dataclasses import dataclass


@dataclass
class Config:
    url: str
    loglevel: str
    companies: dict[str, int]


config = Config(
    url=os.environ['BACKEND_URL'],
    loglevel=os.getenv('LOGLEVEL', 'INFO'),
    companies={
        'wur': os.environ['WUR_COMPANY_ID'],
        'moderna': os.environ['MODERNA_COMPANY_ID'],
    }
)
