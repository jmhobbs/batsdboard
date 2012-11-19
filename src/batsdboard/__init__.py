# Modules/blueprints
from .dashboard import dashboard


class BatsdBoard(object):
    def __init__(self, app, url_prefix='/batsd'):
        self.init_app(app, url_prefix)

    def init_app(self, app, url_prefix='/batsd'):
        app.register_blueprint(dashboard, url_prefix=url_prefix)
