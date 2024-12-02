from typing import Optional
from pydantic import BaseModel


class Player(BaseModel):
    username: str
    id: int
    display_name: Optional[str] = None