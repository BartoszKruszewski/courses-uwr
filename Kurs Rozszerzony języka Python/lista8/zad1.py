import asyncio
from aiohttp import ClientSession
from private import API_KEY

async def fetch_data(session, method, url, params, headers):
    async with session.request(method, url, data=params, headers=headers) as response:
        return await response.json()

requests = [
    (
        'get',
        'https://official-joke-api.appspot.com/random_joke',
        {},
        {}
    ),
    (
        'post',
        'https://text-translator2.p.rapidapi.com/translate',
        {
            "source_language": "en",
            'target_language': 'pl',
            "text": "What is your name?",
        },
        {
            "content-type": "application/x-www-form-urlencoded",
	        "X-RapidAPI-Key": API_KEY,
	        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
        }
    )
]

async def main():
    async with ClientSession() as session:
        responses = [
            fetch_data(session, *request)
            for request in requests
        ]
        pages = await asyncio.gather(*responses)
        [print(page) for page in pages]

asyncio.run(main())
