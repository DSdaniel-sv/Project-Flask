from os import getenv


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevelopmentConfig(BaseConfig):
    pass
class ProductionConfig(BaseConfig):
    pass

environment = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}