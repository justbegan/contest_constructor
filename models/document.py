from pydantic import BaseModel, Field, HttpUrl


class Documents(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    date: int = Field(..., ge=0)
    file_url: HttpUrl = Field(...)
    location: str = Field(..., min_length=1)
    created_at: str = None

    class Config:
        allow_mutation = True
