import os


class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DATABASE_URL = os.environ["DATABASE_URL"]
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    SECRET_KEY = os.environ['SECRET_KEY']
    DATABASE_URL = os.environ["DATABASE_URL"]
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    SECRET_KEY = os.environ['SECRET_KEY']
    DATABASE_TEST_URL = os.environ["DATABASE_URL"]
    TESTING = True


app_config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
