from enum import Enum


discord_message: str = 'message us on Discord (sledge_hammer, regulated) if this happens'


class AIErrors(Enum):
    NO_GEMINI_KEY = f'No Gemini key could be found, {discord_message}'
    STATUS_WAS_NOT_200 = f'The API we use did not return a status code of 200 OK, {discord_message}'


class HTTPSessionErrors(Enum):
    NO_SESSION = f'No HTTP session could be found, {discord_message}'