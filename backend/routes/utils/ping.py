from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get('/ping', summary='Ping the API', tags=['Utility'])
async def ping(request: Request):
    return JSONResponse('pong!')