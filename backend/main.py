from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse, Response, RedirectResponse
from fastapi.requests import Request

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

import aiohttp
from contextlib import asynccontextmanager

from utilities import auth
from utilities.session import AiohttpSessionManager

from routes.ai import (
    gemini,
    cai,
    moderation
)
from routes.nsfw import (
    neko
)
from routes.roblox import (
    bans,
    process_commands,
    server
)
from routes.utils import (
    api
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    session_manager = AiohttpSessionManager()
    app.state.session_manager = session_manager
    app.state.session = await session_manager.startup()
    yield
    await app.state.session_manager.shutdown()


description: str = """
pretty cool API

Main website: https://rac-corp.net/

Bot commands: https://rac-corp.net/docs/commands
"""
limiter = Limiter(key_func=get_remote_address, default_limits=['10/second'])
app = FastAPI(
    title='RAC API', 
    description=description,
    terms_of_service='https://rac-corp.net/legal/terms-of-service',
    license_info={
        'name': 'MIT License',
        'url': 'https://rac-corp.net/legal/license'
    },
    version='0.0.5',
    lifespan=lifespan
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler) # type: ignore
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException):
    return JSONResponse(
        status_code=exception.status_code, 
        content={
            'status': exception.status_code,
            'detail': exception.detail
        }
    )


# AI endpoints


app.include_router(
    gemini.router,
    prefix='/ai',
    dependencies=[Depends(auth.api_key_auth)]
)


app.include_router(
    moderation.router,
    prefix='/ai',
    dependencies=[Depends(auth.api_key_auth)]
)


app.include_router(
    cai.router,
    prefix='/ai',
    dependencies=[Depends(auth.api_key_auth)]
)


# NSFW endpoints


app.include_router(
    neko.router,
    prefix='/nsfw',
    dependencies=[Depends(auth.api_key_auth)]
)


# Roblox endpoints


app.include_router(
    bans.router,
    prefix='/roblox',
    dependencies=[Depends(auth.api_key_auth)]
)


app.include_router(
    process_commands.router,
    prefix='/roblox',
    dependencies=[Depends(auth.api_key_auth)]
)


app.include_router(
    server.router,
    prefix='/roblox',
    dependencies=[Depends(auth.api_key_auth)]
)


# Utility endpoints


app.include_router(
    api.router,
    prefix='/utilities',
    dependencies=[Depends(auth.api_key_auth)]
)


@app.get('/', summary='Don\'t GET this endpoint, it is just a redirect')
@limiter.limit('1/second')
async def root(request: Request):
    return RedirectResponse('https://api.rac-corp.net/docs/', 308)