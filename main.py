from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse, Response, RedirectResponse
from fastapi.requests import Request

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded

from api.utilities import auth
from api.routes.utils import (
    ping
)


limiter = Limiter(key_func=get_remote_address, default_limits=['10/second'])
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler) # type: ignore
app.add_middleware(SlowAPIMiddleware)


app.include_router(
    ping.router,
    prefix='/utilities',
    dependencies=[Depends(auth.api_key_auth)]
)


@app.get('/')
@limiter.limit('10/second')
async def root(request: Request):
    return JSONResponse({'content': 'hello world'})