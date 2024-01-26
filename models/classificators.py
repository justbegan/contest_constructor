from pydantic import BaseModel, Field
from typing import List


class ClassificatorItem(BaseModel):
    title: str = Field(..., min_length=1)
    id: int


class Classificators(BaseModel):
    data: List[ClassificatorItem]
    title: str = Field(..., min_length=1)
