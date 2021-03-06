import os


class Config(object):
    """
    Common configurations
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL')

    SECRET_KEY = 'BC47E778683EA7B8DEAFF8C461BBEd'


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
