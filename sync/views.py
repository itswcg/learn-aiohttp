from aiohttp import web
from sync import db


async def create_msg(request):
    if request.method == 'POST':
        data = await request.post()

        async with request.app['db_engine'].acquire() as conn:
            await db.create_msg(conn, data['fromUserId'], data['toUserId'], data['content'])

        return web.Response(text='Success')

    return web.Response(text='Hello, world')
