""" API config File """
import os


class Config(object):
    """ Parent configuration class """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevelopmentConfig(Config):
    """ Configuration for development environment """
    DEBUG = True


class StagingConfig(Config):
    """ Configuration for the staging environment """
    DEBUG = True


class TestingConfig(Config):
    """ Configuration for the testing environment """
    TESTING = True


class ProductionConfig(Config):
    """ Configuration for the production environment """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'debug': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig
}