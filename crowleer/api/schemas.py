from datetime import date

from typing import Optional

from pydantic import BaseModel, Field


class Job(BaseModel):
    uid: int = Field(ge=1)
    name: str = Field(min_length=2)
    salary: Optional[int]
    region: Optional[str] = Field(min_length=2)
    description: Optional[str] = Field(max_length=100)
    date_published: date
    date_expiring: Optional[date]
    url: str


class Company(BaseModel):

    uid: int = Field(ge=1)
    name: str = Field(min_length=2)
    region: str = Field(min_length=2)
    category: str = Field(min_length=2)
    description: str
