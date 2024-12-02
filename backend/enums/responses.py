from typing import Any
from enum import Enum


def generate_response(
    message: str,
    description: str, 
    status: int,
    detail: str
) -> dict[str, Any]:
    return {
        'description': f'{message}: {description}',
        'content': {
            'application/json': {
                'example': {'status': status, 'detail': detail}
            }
        }
    }


error_500: dict[str, Any] = generate_response(
    'Internal Server Error', 
    'Something happened on our end',
    500,
    'An error message would go here'
)
error_403: dict[str, Any] = generate_response(
    'Forbidden',
    'The request was not authenticated properly',
    403,
    'Forbidden'
)
error_401: dict[str, Any] = generate_response(
    'Unauthorized',
    'The request was not authenticated at all',
    401,
    'Unauthorized'
)
error_400: dict[str, Any] = generate_response(
    'Bad Request',
    'The request body could not be read by the server',
    400,
    'Bad Request'
)


class Responses(Enum):

    # ai endpoints
    GEMINI_RESPONSES = {
        500: error_500,
        403: error_403,
        401: error_401,
        200: {
            'description': 'OK: Successful request',
            'content': {
                'application/json': {
                    'example': {
                        'response': 'The AI\'s response',
                        'totalTime': 'The amount of time it took for the AI to generate its response',
                        'metadata': {
                            'promptTokenCount': 'The token count of the prompt',
                            'responseTokenCount': 'The token count of the response',
                            'totalTokenCount': 'The added total of the prompt and response token counts',
                            'promptLength': 'The amount of characters in the prompt',
                            'responseLength': 'The amount of characters in the response'
                        }
                    }
                }
            }
        }
    }
    TEXT_MODERATION = {
        500: error_500,
        403: error_403,
        401: error_401,
        200: {
            'description': 'Successful request',
            'content': {
                'application/json': {
                    'example': {
                        'flags': 'A list of the flags that the AI marked'
                    }
                }
            }
        }
    }

    # roblox endpoints
    BAN_RESPONSES = {
        500: error_500,
        409: generate_response(
            'Conflict',
            'The user is already banned',
            409,
            'Conflict'
        ),
        404: generate_response(
            'Not Found',
            'The user could not be found',
            404,
            'Not Found'
        ),
        403: error_403,
        401: error_401,
        400: error_400,
    }
    UNBAN_RESPONSES = {
        500: error_500,
        404: generate_response(
            'Not Found',
            'The user is not banned',
            404,
            'Not Found'
        ),
        403: error_403,
        401: error_401,
        400: error_400,
    }
    SERVER_INFO_RESPONSES = {
        500: error_500,
        404: generate_response(
            'Not Found',
            'The requested server could not be found',
            404,
            'Not Found'
        ),
        403: error_403,
        401: error_401,
        400: error_400
    }
    SHUTDOWN_SERVER_RESPONSES = {
        500: error_500,
        404: generate_response(
            'Not Found',
            'The requested server could not be found',
            404,
            'Not Found'
        ),
        403: error_403,
        401: error_401,
        400: error_400
    }

    # utility endpoints
    UTILITY_RESPONSES = {
        500: error_500,
        403: error_403,
        401: error_401
    }