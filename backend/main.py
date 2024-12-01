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
from routes.utils import (
    ping
)
from routes.ai import (
    gemini
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await session_manager.startup()
    yield
    await session_manager.shutdown()


limiter = Limiter(key_func=get_remote_address, default_limits=['10/second'])
app = FastAPI(lifespan=lifespan)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler) # type: ignore
app.add_middleware(SlowAPIMiddleware)
session_manager = AiohttpSessionManager()


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exception: HTTPException):
    return JSONResponse(
        status_code=exception.status_code, 
        content={
            'status': exception.status_code,
            'detail': exception.detail
        }
    )


app.include_router(
    ping.router,
    prefix='/utilities',
    dependencies=[Depends(auth.api_key_auth)]
)


app.include_router(
    gemini.router,
    prefix='/ai/gemini',
    dependencies=[Depends(auth.api_key_auth)]
)


@app.get('/', summary='Don\'t GET this endpoint, it is just a redirect')
@limiter.limit('1/second')
async def root(request: Request):
    return RedirectResponse('https://api.rac-corp.net/docs/', 308)