import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(SQLALCHEMY_DATABASE_URI, False)


class Development(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False