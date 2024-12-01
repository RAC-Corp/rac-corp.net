from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response, RedirectResponse


app = FastAPI()


@app.get('/')
async def root():
    return JSONResponse({'content': 'hello world'})