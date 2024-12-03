from enum import Enum


discord_message: str = 'message us on Discord (sledge_hammer, regulated) if this happens'


class AIErrors(Enum):
    NO_CLOUDFLARE_KEY = f'No Cloudflare key could be found, {discord_message}'
    NO_GEMINI_KEY = f'No Gemini key could be found, {discord_message}'
    STATUS_WAS_NOT_200 = f'The API we use did not return a status code of 200 OK, {discord_message}'


class HTTPSessionErrors(Enum):
    NO_SESSION = f'No HTTP session could be found, {discord_message}'


class RobloxErrors(Enum):
    NO_PLAYER_ARGUMENT = 'No player ID or username could be found in the request body'
    NO_IISR_KEY = f'No IISR key could be found, {discord_message}'