from pydantic import BaseModel, Field

from services.fields.utctime import get_current_utc_time


class Comments(BaseModel):
    statement_oid: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)
    create_at: int = get_current_utc_time()
    author: int = None
