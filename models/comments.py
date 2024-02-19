from pydantic import BaseModel, Field


class Comments(BaseModel):
    statement_oid: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)
