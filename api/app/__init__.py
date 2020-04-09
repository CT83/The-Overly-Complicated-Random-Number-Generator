from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.api.tasks.tasks import TasksRes
from config import config
from shared.utils import db_connection_successful


def create_app(config_name):
    app = Flask(__name__, )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app)

    api = Api(app)
    api.add_resource(TasksRes, '/tasks')

    from shared.factories import rq
    rq.init_app(app)

    # Database
    from shared.factories import db

    db.app = app
    db.init_app(app)
    with app.app_context():
        assert db_connection_successful(db)

    from shared.log_manager import LogManager
    app = LogManager().init_app(app)

    return app
