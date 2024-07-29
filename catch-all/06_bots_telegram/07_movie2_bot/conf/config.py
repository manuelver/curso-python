import os

from dotenv import load_dotenv


load_dotenv('.env')


class Config(object):

    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    DATABASE_URL = os.getenv('DATABASE_URL')
    TELEGRAM_BOT_API = os.getenv('TELEGRAM_BOT_API')
    LOG_FILE = 'logs/movie2_bot.log'
    QUIZ_LANG = 'es'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'
    SESSION_EXPIRATION_TIME = 30


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_EXPIRATION_TIME = 10


class TestingConfig(Config):
    TESTING = True
