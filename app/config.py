import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'WUQJ877peYBn6S2T')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'todo.db')


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # EMAIL_HOST =
    # EMAIL_PORT =
    # EMAIL_SSL =
    # EMAIL_USER =
    # EMAIL_PASS =
    # EMAIL_FROM_ADDRESS =


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


configuration = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    test=TestingConfig
)
