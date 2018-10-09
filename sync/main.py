import logging

from aiohttp import web
from sync.db import init_db, close_db
from sync.routes import setup_routes

log = logging.getLogger(__name__)


async def init_app():
    app = web.Application()

    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    setup_routes(app)
    return app


def main():
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
