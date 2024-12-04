from typing import Optional, Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse

import os
import time
import aiohttp

from models.ai_models import CloudflareImageRequestModel
from enums.errors import HTTPSessionErrors, AIErrors
from enums.responses import Responses


# TODO: do something