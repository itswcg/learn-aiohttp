import json

import aiohttp
import asyncio

payload = {'fromUserId': '1', 'toUserId': '2', 'content': 'hello, world'}
headers = {'content-type': 'application/json'}


async def fetch(session, url):
    async with session.post(url, data=json.dumps(payload), headers=headers) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://0.0.0.0:8080/')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [main() for i in range(5000)]
    loop.run_until_complete(asyncio.wait(tasks))
