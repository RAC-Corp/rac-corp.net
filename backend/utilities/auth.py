from typing import Annotated, Any

import os

from fastapi import HTTPException, Security, status, Depends
from fastapi.security import APIKeyHeader, HTTPBearer, HTTPAuthorizationCredentials


api_keys: dict[str, Any] = {
    'testkey': os.environ.get('testkey'),
    'publictestkey': os.environ.get('publictestkey'),
    'insecurekey': os.environ.get('insecurekey')
}


api_key_header = APIKeyHeader(name='Authorization')
bearer = HTTPBearer()


async def api_key_auth(credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer)]):
    for value in api_keys.values():
        if value in credentials.credentials:
            return value
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unauthorized'
    )