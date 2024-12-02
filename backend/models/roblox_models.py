from typing import Optional
from pydantic import BaseModel


class Player(BaseModel):
    username: Optional[str] = None
    id: Optional[int] = None


class Server(BaseModel):
    id: str