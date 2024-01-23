from pydantic import BaseModel, Field


class Contests(BaseModel):
    title: str = Field(..., min_length=1)
    unique_name: str = Field(..., min_length=1)
    active: bool
