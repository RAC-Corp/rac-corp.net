from typing import Union, Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import aiohttp

from utilities.moderation import moderate_text_input
from enums.errors import HTTPSessionErrors
from enums.responses import Responses


router = APIRouter(prefix='/moderation')


@router.get(
    '/text', 
    summary='Classify text based on its inappropiateness', 
    tags=['AI'],
    responses={**Responses.TEXT_MODERATION.value}
)
async def moderate_text(request: Request, text: str):
    session: Optional[aiohttp.ClientSession] = request.app.state.session
    if not session:
        raise HTTPException(500, HTTPSessionErrors.NO_SESSION.value)

    flags: Union[list, str] = await moderate_text_input(request.app.state.session, text)
    return JSONResponse({'results': flags})