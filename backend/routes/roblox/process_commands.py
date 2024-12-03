from typing import Optional, Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import os
import aiohttp

from models.roblox_models import Server, Game, CommandModel
from enums.responses import Responses
from enums.errors import HTTPSessionErrors, RobloxErrors


router = APIRouter()
iisr_key: Optional[str] = os.environ.get('iisr_key')
universe_ids: dict[str, int] = {
    'iisr': 4791664217
}
iisr_queue: str = f'https://apis.roblox.com/v2/universes/{universe_ids["iisr"]}/memory-store/queues/IISRCOMMANDSQUEUE/items'


@router.post(
    '/process-commands', 
    summary='Send and queue a command to our Roblox games', 
    tags=['Server'],
    responses={**Responses.PLACEHOLDER_RESPONSES.value},
    deprecated=True
)
async def process_command(request: Request, command: CommandModel):
    session: Optional[aiohttp.ClientSession] = request.app.state.session
    if not session:
        raise HTTPException(500, HTTPSessionErrors.NO_SESSION.value)
    
    if not iisr_key:
        raise HTTPException(500, RobloxErrors.NO_IISR_KEY.value)
    
    headers: dict[str, str] = {
        'x-api-key': iisr_key
    }
    json: dict[str, Any] = {
        'data': f'{command.username}: {command}',
        'ttl': '15m'
    }
    async with session.post(iisr_queue, headers=headers, json=json) as resp:
        if resp.status != 200:
            raise HTTPException(500, f'Roblox gave us the middle finger: HTTP {resp.status}')
        
        data: Any = await resp.json()
        return JSONResponse(data)

    # return JSONResponse('Done', 204)