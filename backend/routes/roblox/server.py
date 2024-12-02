from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

from models.roblox_models import Server
from enums.responses import Responses


router = APIRouter(prefix='/server')


@router.delete(
    '/shutdown', 
    summary='Shutdown a server', 
    tags=['Server'],
    responses={**Responses.SHUTDOWN_SERVER_RESPONSES.value}
)
async def shutdown_server(request: Request, server: Server):
    return JSONResponse({'response': 'not active yet'})


@router.get(
    '/info', 
    summary='Get the info of a server', 
    tags=['Server'],
    responses={**Responses.SERVER_INFO_RESPONSES.value}
)
async def get_server_info(request: Request, server_id: str):
    return JSONResponse({'response': 'not active yet'})