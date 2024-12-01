from typing import Optional
from pydantic import BaseModel


class GeminiRequestModel(BaseModel):
    prompt: str
    debug: Optional[bool] = False