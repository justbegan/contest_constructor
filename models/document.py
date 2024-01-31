from pydantic import BaseModel, Field


class Documents(BaseModel):
    title: str = Field(..., min_length=1)
