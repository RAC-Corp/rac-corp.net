from typing import Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import psutil
import os

from enums.responses import Responses


router = APIRouter()


@router.get(
    '/ping', 
    summary='Ping the API', 
    tags=['Utility'],
    responses={**Responses.PING_RESPONSES.value}
)
async def ping(request: Request):
    # TODO: add responses argument
    return JSONResponse({'response': 'pong!'})


@router.get(
    '/usage', 
    summary='Get the process usages of the API',
    tags=['Utility'],
    responses={**Responses.USAGE_RESPONSES.value}
)
async def usage(request: Request):
    pid: int = os.getpid()
    process = psutil.Process(pid)
    cpu_usage: float = process.cpu_percent(1)
    memory_info = process.memory_info()
    rss_memory: Any = memory_info.rss
    vms_memory: Any = memory_info.vms
    
    return JSONResponse(
        {
            'usage': {
                'cpu': f'{cpu_usage}%',
                'rssMem': f'{rss_memory / (1024 ** 2):.2f} MB',
                'vmsMem': f'{vms_memory / (1024 ** 2):.2f} MB',
            }
        }
    )