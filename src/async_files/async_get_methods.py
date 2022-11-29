import asyncio
from typing import List

from aiohttp import ClientSession

results = {}

async def pull_of_responses(session, url: str) -> None:
    http_methods = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
    available_methods = {}
    for method in http_methods:
        async with session.request(method=method, url=url) as resp:
            if resp.status != 405:
                available_methods[method] = resp.status
    results.setdefault(url, available_methods)


async def gather_response(urls: List[str]) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(pull_of_responses(session, url))
        await asyncio.gather(*tasks) # collect tasks inside the manager!!!!


def get_methods_from_url(urls: List[str]) -> dict:
    asyncio.run(gather_response(urls))
    return results