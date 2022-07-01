import os
from dataclasses import dataclass


@dataclass
class Config:

    app_host: str
    app_port: int


config = Config(
    app_host=os.environ['APP_HOST'],
    app_port=int(os.environ['APP_PORT']),
)
