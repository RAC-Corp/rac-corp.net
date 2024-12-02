from enum import Enum


class Responses(Enum):
    GEMINI_RESPONSES = {
        500: {'description': 'Something happened on our end'},
        403: {'description': 'The request was not authorized properly'},
        401: {'description': 'The request was not authorized at all'},
    }
    BANS_RESPONSES = {
        500: {'description': 'Something happened on our end'},
        404: {'description': 'The user is not banned or could not be found'},
        403: {'description': 'The request was not authorized properly'},
        401: {'description': 'The request was not authorized at all'},
        400: {'description': 'The request body could not be read by the server'},
    }