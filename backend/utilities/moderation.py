from typing import Optional, Any, Union

import aiohttp
import os


url: str = 'https://api.openai.com/v1/moderations'
openai_key: Optional[str] = os.environ.get('openai_key')


async def moderate_text_input(session: aiohttp.ClientSession, text: str) -> Union[list, str]:
    """Classify and flag text inputs

    Args:
        session (aiohttp.ClientSession): The aiohttp session to use
        text (str): The text input to classify and flag

    Returns:
        data (Union[dict[str, Any], str]): The JSON data returned by OpenAI
    """

    if not openai_key:
        return 'OpenAI key was not found'

    headers: dict[str, str] = {
        'Authorzation': f'Bearer {openai_key}',
        'Content-Type': 'application/json'
    }
    json: dict[str, str] = {
        'model': 'omni-moderation-latest',
        'input': text
    }

    async with session.post(url, headers=headers, json=json) as resp:
        if resp.status != 200:
            return f'HTTP {resp.status}: {resp.reason}'
        
        data: dict[str, Any] = await resp.json()
        categories: dict[str, bool] = data['results'][0]['categories']
        flagged: list[str] = []
        
        for category, is_true in categories.items():
            if is_true:
                flagged.append(category)
        
        return flagged