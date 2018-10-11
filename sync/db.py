import sqlalchemy as sa

from aiomysql.sa import create_engine

metadata = sa.MetaData()

# msg = sa.Table('msg', metadata,
#                sa.Column('id', sa.Integer, primary_key=True),
#                sa.Column('fromUserId', sa.String(10)),
#                sa.Column('toUserId', sa.String(10)),
#                sa.Column('content', sa.String(1000)))


async def init_db(app):
    engine = await create_engine(user='root',
                                 db='message',
                                 host='127.0.0.1',
                                 password='wcg')
    app['db_engine'] = engine
    return engine


async def close_db(app):
    app['db_engine'].close()
    await app['db_engine'].wait_closed()


async def create_msg(conn, fromUserId, toUserId, content):
    tx = await conn.begin()
    # ms = msg.insert().values(fromUserId=fromUserId, toUserId=toUserId, content=content)
    await conn.execute("INSERT INTO msg (fromUserId, toUserId, content) VALUES (%s, %s, %s)", (fromUserId, toUserId, content))
    await tx.commit()
