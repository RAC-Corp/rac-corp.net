from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from ...models.roblox_models import Player


router = APIRouter(prefix='/bans')


@router.post('/create', summary='Ban a player with their user ID or username')
async def ban_create(request: Request, player: Player):
    return JSONResponse({'response': 'not active yet'})


@router.delete('/remove', summary='Ban a player with their user ID or username')
async def ban_remove(request: Request, player: Player):
    return JSONResponse({'response': 'not active yet'})