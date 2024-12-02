from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from models.roblox_models import Player
from enums.responses import Responses


router = APIRouter(prefix='/bans')


@router.post(
    '/create/temp', 
    summary='Ban a player with their user ID or username', 
    tags=['Bans'],
    responses={**Responses.BANS_RESPONSES.value}
)
async def temp_ban_create(request: Request, player: Player, time: str):
    return JSONResponse({'response': 'not active yet'})


@router.post(
    '/create/perm', 
    summary='Permanently ban a player with their user ID or username', 
    tags=['Bans'],
    responses={**Responses.BANS_RESPONSES.value}
)
async def perm_ban_create(request: Request, player: Player):
    return JSONResponse({'response': 'not active yet'})


@router.delete(
    '/remove', 
    summary='Unban a player with their user ID or username',
    tags=['Bans'],
    responses={**Responses.BANS_RESPONSES.value}
)
async def ban_remove(request: Request, player: Player):
    return JSONResponse({'response': 'not active yet'})