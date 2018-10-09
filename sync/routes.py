from sync.views import create_msg


def setup_routes(app):
    app.router.add_get('/', create_msg, name='create-msg')
    app.router.add_post('/', create_msg, name='create-msg')
