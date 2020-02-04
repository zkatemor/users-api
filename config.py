import os


class Config:
    DEBUG = True
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQL_ALCHEMY_DB_URL = 'sqlite:///%s/users.db?check_same_thread=False' % APPLICATION_DIR
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'
