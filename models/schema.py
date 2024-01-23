from pydantic import BaseModel, Field


class Schemas(BaseModel):
    title: str = Field(..., min_length=1)
    properties: dict
    required: list
    type: str = Field(..., min_length=1)
    contest_oid: str = Field(..., min_length=1)
