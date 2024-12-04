from typing import Optional, Any, Union

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import os
import time
import aiohttp

from models.ai_models import CharacterAIRequestModel
from enums.errors import HTTPSessionErrors, AIErrors
from enums.responses import Responses


router = APIRouter(prefix='/cai')
url: str = 'https://plus.character.ai/chat/streaming/'
cai_key: Optional[str] = os.environ.get('cai_key')
chat_key: Optional[str] = os.environ.get('cai_chat_key')
cai_tgt: Optional[str] = os.environ.get('cai_tgt')


def extract_text(data: str) -> str:
    try:
        last_text_index: int = data.rfind('"text":')
        last_uuid_index: int = data.rfind('", "uuid":')
        if last_text_index == -1 or last_uuid_index == -1:
            return 'text extraction error'

        start_index: int = last_text_index + len('"text":')
        extracted_text: str = data[start_index:last_uuid_index].strip().strip('"')

        return extracted_text
    except Exception as e:
        return str(e)


@router.post(
    '/create',
    summary='Chat with a Character.AI bot',
    tags=['AI'],
    responses={**Responses.CHARACTER_AI_RESPONSES.value}
)
async def create_cai(request: Request, data: CharacterAIRequestModel, raw: bool = False):
    if len(data.prompt) > 1000:
        raise HTTPException(413, 'Prompt content too long (less than or equal to 1000 characters)')
    
    if not cai_key:
        raise HTTPException(500, AIErrors.NO_CAI_KEY.value)
    if not chat_key:
        raise HTTPException(500, AIErrors.NO_CAI_CHAT_KEY.value)
    if not cai_tgt:
        raise HTTPException(500, AIErrors.NO_CAI_TGT.value)
    
    session: Optional[aiohttp.ClientSession] = request.app.state.session
    if not session:
        raise HTTPException(500, HTTPSessionErrors.NO_SESSION)
    
    headers: dict[str, str] = {
        'Authorization': cai_key
    }
    json: dict[str, str] = {
        'history_external_id': chat_key,
        'text': data.prompt,
        'tgt': cai_tgt
    }
    start_time: float = time.time()
    async with session.post(url, headers=headers, json=json) as resp:
        if resp.status != 200:
            raise HTTPException(500, f'C.AI gave us the middle finger: HTTP {resp.status}')

        end_time: float = time.time()
        total_time: float = end_time - start_time
        if not raw:
            text: str = await resp.text()
            content: str = extract_text(text)
            return JSONResponse({'response': content, 'totalTime': total_time})
        else:
            try:
                json_data: Any = await resp.json()
            except:
                raise HTTPException(500, 'JSONifying response data failed')
            return JSONResponse({'response': json_data, 'totalTime': total_time})
        

@router.get(
    '/history',
    summary='Get the history of the current C.AI chat',
    tags=['AI'],
    responses={**Responses.PLACEHOLDER_RESPONSES.value}
)
async def history_cai(request: Request):
    if not cai_key:
        raise HTTPException(500, AIErrors.NO_CAI_KEY.value)
    if not chat_key:
        raise HTTPException(500, AIErrors.NO_CAI_CHAT_KEY.value)
    if not cai_tgt:
        raise HTTPException(500, AIErrors.NO_CAI_TGT.value)
    
    '''session: Optional[aiohttp.ClientSession] = request.app.state.session
    if not session:
        raise HTTPException(500, HTTPSessionErrors.NO_SESSION)'''
    
    return JSONResponse({'wip endpoint'})