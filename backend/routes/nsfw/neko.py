from typing import Optional, Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import aiohttp

from enums.errors import HTTPSessionErrors
from enums.responses import Responses


router = APIRouter(prefix='/neko')


@router.get(
    '/image', 
    summary='Hi Harrisson', 
    tags=['NSFW'],
    responses={**Responses.PLACEHOLDER_RESPONSES.value}
)
async def neko_nsfw_image(request: Request):
    session: Optional[aiohttp.ClientSession] = request.app.state.session
    if not session:
        raise HTTPException(500, HTTPSessionErrors.NO_SESSION.value)
    
    url: str = 'https://purrbot.site/api/img/nsfw/neko/img'
    async with session.get(url) as resp:
        if resp.status != 200:
            raise HTTPException(500, 'Service we use gave us the middle finger')
        
        data: Any = await resp.json()
        return JSONResponse(data['url'])