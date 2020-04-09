#!/usr/bin/env python
import os

from flask_migrate import Migrate
from flask_sqlalchemy import Model

from app import create_app
from shared.factories import db

env = os.environ.get('FLASK_ENV', 'default')
app = create_app(os.environ.get('FLASK_ENV', 'default'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, Model=Model)

