from pydantic import BaseModel, Field


class News(BaseModel):
    title: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)
    hide: bool = False
