from enum import Enum


class Responses(Enum):

    # ai endpoints
    GEMINI_RESPONSES = {
        500: {
            'description': 'Internal Server Error: Something happened on our end',
            'content': {
                'application/json': {
                    'example': {'status': 500, 'detail': 'An error message would go here'}
                }
            }
        },
        403: {
            'description': 'Forbidden: The request was not authorized properly',
            'content': {
                'application/json': {
                    'example': {'status': 403, 'detail': 'Forbidden'}
                }
            }
        },
        401: {
            'description': 'Unauthorized: The request was not authorized at all',
            'content': {
                'application/json': {
                    'example': {'status': 401, 'detail': 'Unauthorized'}
                }
            }
        },
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
        500: {
            'description': 'Internal Server Error: Something happened on our end',
            'content': {
                'application/json': {
                    'example': {'status': 500, 'detail': 'An error message would go here'}
                }
            }
        },
        409: {
            'description': 'Conflict: The user is already banned',
            'content': {
                'application/json': {
                    'example': {'status': 409, 'detail': 'Conflict'}
                }
            }
        },
        404: {
            'description': 'Not Found: The user could not be found',
            'content': {
                'application/json': {
                    'example': {'status': 404, 'detail': 'Not Found'}
                }
            }
        },
        403: {
            'description': 'Forbidden: The request was not authorized properly',
            'content': {
                'application/json': {
                    'example': {'status': 403, 'detail': 'Forbidden'}
                }
            }
        },
        401: {
            'description': 'Unauthorized: The request was not authorized at all',
            'content': {
                'application/json': {
                    'example': {'status': 401, 'detail': 'Unauthorized'}
                }
            }
        },
        400: {
            'description': 'Bad Request: The request body could not be read by the server',
            'content': {
                'application/json': {
                    'example': {'status': 400, 'detail': 'Bad Request'}
                }
            }
        },
    }
    UNBAN_RESPONSES = {
        500: {
            'description': 'Internal Server Error: Something happened on our end',
            'content': {
                'application/json': {
                    'example': {'status': 500, 'detail': 'An error message would go here'}
                }
            }
        },
        404: {
            'description': 'Not Found: The user is not banned',
            'content': {
                'application/json': {
                    'example': {'status': 404, 'detail': 'Not Found'}
                }
            }
        },
        403: {
            'description': 'Forbidden: The request was not authorized properly',
            'content': {
                'application/json': {
                    'example': {'status': 403, 'detail': 'Forbidden'}
                }
            }
        },
        401: {
            'description': 'Unauthorized: The request was not authorized at all',
            'content': {
                'application/json': {
                    'example': {'status': 401, 'detail': 'Unauthorized'}
                }
            }
        },
        400: {
            'description': 'Bad Request: The request body could not be read by the server',
            'content': {
                'application/json': {
                    'example': {'status': 400, 'detail': 'Bad Request'}
                }
            }
        },
    }

    # utility endpoints
    UTILITY_RESPONSES = {

    }