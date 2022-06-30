from datetime import date

from pydantic import BaseModel, Field


class JobModel(BaseModel):
    uid: int = Field(ge=1)
    name: str = Field(min_length=2)
    salary: int
    description: str = Field(max_length=100)
    date_published: date
    date_expiring: date
    url: str

    class Config:
        orm_mode = True


class CompanyModel(BaseModel):

    uid: int = Field(ge=1)
    name: str = Field(min_length=2)
    region: str = Field(min_length=2)
    category: str = Field(min_length=2)
    description: str

    class Config:
        orm_mode = True
