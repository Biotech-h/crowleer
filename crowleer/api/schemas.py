from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


MAX_DESCRIPTION_LENGTH = 4096


class Job(BaseModel):
    uid: int
    name: str = Field(min_length=2)
    salary: Optional[int]
    region: Optional[str] = Field(min_length=2)
    description: Optional[str] = Field(max_length=MAX_DESCRIPTION_LENGTH)
    date_published: Optional[date]
    date_expiring: Optional[date]
    url: str
