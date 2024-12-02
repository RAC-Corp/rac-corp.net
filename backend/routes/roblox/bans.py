from typing import Union

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from models.roblox_models import Player
from enums.responses import Responses
from enums.errors import RobloxErrors


router = APIRouter(prefix='/bans')


# TODO: add 200 status code responses
@router.post(
    '/create/temp', 
    summary='Ban a player with their user ID or username', 
    tags=['Bans'],
    responses={**Responses.BAN_RESPONSES.value}
)
async def temp_ban_create(request: Request, player: Player, time: str):
    search: Union[str, int]
    if not player.id and player.username:
        search = player.username
    elif not player.username and player.id:
        search = player.id
    else:
        raise HTTPException(400, RobloxErrors.NO_PLAYER_ARGUMENT.value)

    return JSONResponse({'response': 'not active yet', 'provided': search})


@router.post(
    '/create/perm', 
    summary='Permanently ban a player with their user ID or username', 
    tags=['Bans'],
    responses={**Responses.BAN_RESPONSES.value}
)
async def perm_ban_create(request: Request, player: Player):
    search: Union[str, int]
    if not player.id and player.username:
        search = player.username
    elif not player.username and player.id:
        search = player.id
    else:
        raise HTTPException(400, RobloxErrors.NO_PLAYER_ARGUMENT.value)

    return JSONResponse({'response': 'not active yet', 'provided': search})


@router.delete(
    '/remove', 
    summary='Unban a player with their user ID or username',
    tags=['Bans'],
    responses={**Responses.UNBAN_RESPONSES.value}
)
async def ban_remove(request: Request, player: Player):
    search: Union[str, int]
    if not player.id and player.username:
        search = player.username
    elif not player.username and player.id:
        search = player.id
    else:
        raise HTTPException(400, RobloxErrors.NO_PLAYER_ARGUMENT.value)

    return JSONResponse({'response': 'not active yet', 'provided': search})