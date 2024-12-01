from typing import Union
import aiohttp


class AiohttpSessionManager:
    def __init__(self) -> None:
        self.session = None

    async def startup(self) -> bool:
        if not self.session:
            self.session = aiohttp.ClientSession()
            return True
        else:
            return False

    async def shutdown(self):
        if self.session:
            await self.session.close()

    async def get_session(self) -> Union[aiohttp.ClientSession, None]:
        if self.session:
            return self.session
        else:
            return None