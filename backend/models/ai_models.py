from typing import Optional
from pydantic import BaseModel


class GeminiRequestModel(BaseModel):
    prompt: str
    debug: Optional[bool] = False


class CloudflareImageRequestModel(BaseModel):
    pass


class CharacterAIRequestModel(BaseModel):
    prompt: str