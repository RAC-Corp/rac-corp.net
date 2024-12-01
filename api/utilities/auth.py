from typing import Annotated

import os

from fastapi import HTTPException, Security, status, Depends
from fastapi.security import APIKeyHeader, HTTPBearer, HTTPAuthorizationCredentials


API_KEY = os.environ.get('testkey') or ''


api_key_header = APIKeyHeader(name='Authorization')
bearer = HTTPBearer()


async def api_key_auth(credentials: Annotated[HTTPAuthorizationCredentials, Depends(bearer)]):
    if API_KEY in credentials.credentials:
        return API_KEY
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unauthorized'
    )