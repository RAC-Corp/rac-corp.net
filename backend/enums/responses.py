from enum import Enum   


class Responses(Enum):
    GEMINI_RESPONSES = {
        500: {'detail': 'Something happened on our end'},
        403: {'detail': 'The request was not authorized properly'},
        401: {'detail': 'The request was not authorized at all'},
    }
    BANS_RESPONSES = {
        500: {'detail': 'Something happened on our end'},
        404: {'detail': 'The user is not banned or could not be found'},
        403: {'detail': 'The request was not authorized properly'},
        401: {'detail': 'The request was not authorized at all'},
    }