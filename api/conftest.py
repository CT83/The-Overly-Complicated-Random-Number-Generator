import os
import sys

import pytest

sys.path.append(os.getcwd())

TEST_USER = "test_user"
TEST_PASSWORD = "test_pass"


@pytest.fixture
def config():
    return 'testing'


@pytest.fixture
def app():
    # Set dummy env vars to prevent errors
    os.environ['POSTGRES_USER'] = "x"
    os.environ['POSTGRES_PASSWORD'] = "x"
    os.environ['POSTGRES_DB'] = ""
    os.environ['DBHOST'] = "x"
    os.environ['DBPORT'] = "x"
    os.environ['REDIS_PORT'] = "x"
    os.environ['REDIS_HOST'] = "x"

    from app import create_app
    from shared.utils import create_dir_if_not_exists
    create_dir_if_not_exists('temp')

    app = create_app('testing')

    with app.app_context():
        from shared.factories import db
        db.create_all()
        yield app
        db.drop_all()


def cleanup_dirs_and_db():
    try:
        import shutil
        shutil.rmtree("temp")
    except:
        pass
