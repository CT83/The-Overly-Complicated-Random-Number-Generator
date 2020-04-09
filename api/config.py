import os

from shared.utils import generate_random_hash

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    FILE_STORAGE = 'data'
    OLDER_IMAGES_TO_DELETE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # Database
    DBUSER = os.environ.get('POSTGRES_USER')
    DBPASS = os.environ['POSTGRES_PASSWORD']
    DBHOST = os.environ['DBHOST']
    DBPORT = os.environ['DBPORT']
    DBNAME = os.environ['POSTGRES_DB']

    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
            user=DBUSER,
            passwd=DBPASS,
            host=DBHOST,
            port=DBPORT,
            db=DBNAME)

    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']

    RQ_REDIS_URL = 'redis://{}:{}'.format(redis_host, redis_port)


class TestingConfig(Config):
    TESTING = True
    DB_FILE_NAME = 'temp/test_{}.db'.format(generate_random_hash())
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, DB_FILE_NAME)
    APP_NAME = os.environ.get('APP_NAME')
    RQ_CONNECTION_CLASS = 'fakeredis.FakeStrictRedis'


class ProductionConfig(Config):
    # Database
    DBUSER = os.environ.get('POSTGRES_USER')
    DBPASS = os.environ['POSTGRES_PASSWORD']
    DBHOST = os.environ['DBHOST']
    DBPORT = os.environ['DBPORT']
    DBNAME = os.environ['POSTGRES_DB']

    SQLALCHEMY_DATABASE_URI = \
        'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
            user=DBUSER,
            passwd=DBPASS,
            host=DBHOST,
            port=DBPORT,
            db=DBNAME)
    redis_host = os.environ['REDIS_HOST']
    redis_port = os.environ['REDIS_PORT']

    RQ_REDIS_URL = 'redis://{}:{}'.format(redis_host, redis_port)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
