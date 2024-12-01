from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from models.ai_models import GeminiRequestModel
from utilities.session import AiohttpSessionManager


router = APIRouter()


@router.post('/create', summary='Talk to Google Gemini AI')
async def ping(request: Request, data: GeminiRequestModel):
    session = await AiohttpSessionManager().get_session()
    return JSONResponse('not complete')