from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import aiohttp

from models.roblox_models import Server, Game
from enums.responses import Responses
from enums.errors import HTTPSessionErrors


router = APIRouter()


@router.post(
    '/process-commands', 
    summary='Send and queue a command to our Roblox games', 
    tags=['Server'],
    responses={**Responses.PLACEHOLDER_RESPONSES.value}
)
async def shutdown_server(request: Request, game: Game, server: Server):
    session: Optional[aiohttp.ClientSession] = request.app.state.session
    if not session:
        raise HTTPException(500, HTTPSessionErrors.NO_SESSION.value)
    return JSONResponse('wip')