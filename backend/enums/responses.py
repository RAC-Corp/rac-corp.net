from enum import Enum


class Responses(Enum):

    # ai endpoints
    GEMINI_RESPONSES = {
        500: {'description': 'Internal Server Error: Something happened on our end'},
        403: {'description': 'Forbidden: The request was not authorized properly'},
        401: {'description': 'Unauthorized: The request was not authorized at all'},
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

    # roblox endpoints
    BAN_RESPONSES = {
        500: {'description': 'Internal Server Error: Something happened on our end'},
        409: {'description': 'Conflict: The user is already banned'},
        404: {'description': 'Not Found: The user could not be found'},
        403: {'description': 'Forbidden: The request was not authorized properly'},
        401: {'description': 'Unauthorized: The request was not authorized at all'},
        400: {'description': 'Bad Request: The request body could not be read by the server'},
    }
    UNBAN_RESPONSES = {
        500: {'description': 'Internal Server Error: Something happened on our end'},
        404: {'description': 'Not Found: The user is not banned yet'},
        403: {'description': 'Forbidden: The request was not authorized properly'},
        401: {'description': 'Unauthorized: The request was not authorized at all'},
        400: {'description': 'Bad Request: The request body could not be read by the server'},
    }

    # utility endpoints
    UTILITY_RESPONSES = {

    }