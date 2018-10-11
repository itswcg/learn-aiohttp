import json

import aiohttp
import asyncio
import requests

payload = {'fromUserId': '1', 'toUserId': '2', 'content': 'hello, world'}
headers = {'content-type': 'application/json'}

header = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}


async def fetch(session, url):
    async with session.post(url, data=json.dumps(payload), headers=headers) as response:
        return await response.text()


async def getch(session, url):
    async with session.get(url, headers=header) as response:
        # return await response.text()
        return


async def main():
    async with aiohttp.ClientSession() as session:
        # html = await fetch(session, 'http://0.0.0.0:8080/')
        html = await getch(session, 'http://blog.itswcg.com')
        print(html)


def test():
    requests.get('http://blog.itswcg.com')
    print('success')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [main() for i in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))
    # for _ in range(100):
    #     test()
