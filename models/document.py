from pydantic import BaseModel, Field


class Documents(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    date: int = Field(..., ge=0)
    file_url: str = Field(..., min_length=1)
    created_at: str = None

    class Config:
        allow_mutation = True
