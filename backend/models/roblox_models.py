from typing import Optional
from pydantic import BaseModel


class Player(BaseModel):
    username: Optional[str] = None
    id: Optional[int] = None


class Server(BaseModel):
    id: str


class Game(BaseModel):
    id: Optional[int]
    universe_id: int


class CommandModel(BaseModel):
    username: str
    command: str