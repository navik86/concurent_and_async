import asyncio
from aiohttp import ClientSession


async def single_response(method: str, url: str) -> dict:
    async with ClientSession() as session:
        available_methods = {}
        async with session.request(method=method, url=url) as resp:
            if resp.status != 405:
                available_methods[method] = resp.status
            return available_methods


async def gather_response(url):
    methods = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
    tasks = []
    for method in methods:
        tasks.append(asyncio.create_task(single_response(method, url)))
    results = await asyncio.gather(*tasks)
    return results


def get_methods_from_url(url: str) -> list:
    return asyncio.run(gather_response(url))