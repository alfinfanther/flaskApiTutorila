import configparser
config_parser = configparser.ConfigParser()
config_parser.read('config.ini')


class Config(object):
    """
    Common configurations
    """
    

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}/{3}'.format(
        config_parser['DBDEV']['DB_USER'],
        config_parser['DBDEV']['DB_PASS'],
        config_parser['DBDEV']['DB_HOST'],
        config_parser['DBDEV']['DB_NAME']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = config_parser['DEFAULT']['SECRET_KEY']


class ProductionConfig(Config):
    """
    Production configurations
    """
    
    DEBUG = False
