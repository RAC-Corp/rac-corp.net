from typing import Optional, Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import os
import time

from models.ai_models import GeminiRequestModel
from utilities.session import AiohttpSessionManager
from enums.errors import HTTPSessionErrors, AIErrors


router = APIRouter()
gemini_key: Optional[str] = os.environ.get('gemini_key')
url: str = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent'


@router.post('/create', summary='Talk to Google Gemini AI')
async def ping(request: Request, data: GeminiRequestModel):
    if len(data.prompt) > 2000:
        raise HTTPException(
            413,
            'Prompt content too long (less than or equal to 2000 characters)'
        )
    if not gemini_key:
        raise HTTPException(500, AIErrors.NO_GEMINI_KEY.value)
    
    session = await AiohttpSessionManager().get_session()
    if not session:
        raise HTTPException(500, HTTPSessionErrors.NO_SESSION.value)

    params: dict[str, str] = {
        'key': gemini_key
    }
    json: dict[str, Any] = {
        'contents': [{
            'parts': [{'text': data.prompt}]
        }]
    }
    start_time: float = time.time()
    async with session.post(url, params=params, json=json) as resp:
        if resp.status != 200:
            raise HTTPException(500, AIErrors.STATUS_WAS_NOT_200.value)
        
        end_time: float = time.time()
        total_time: float = end_time - start_time
        json_data: Any = await resp.json()
        response: str = json_data['candidates'][0]['content']['parts'][0]['text']

        if data.debug:
            metadata: dict[str, int] = json_data['usageMetadata']
            ptc: int = metadata['promptTokenCount']
            ctc: int = metadata['candidatesTokenCount']
            ttc: int = metadata['totalTokenCount']
            return JSONResponse(
                {
                    'response': response,
                    'totalTime': total_time, 
                    'metadata': {
                        'promptTokenCount': ptc,
                        'responseTokenCount': ctc,
                        'totalTokenCount': ttc,
                        'promptLength': len(data.prompt),
                        'responseLength': len(response)
                    }
                },
                200
            )
        else:
            return JSONResponse({'response': response, 'totalTime': total_time}, 200)