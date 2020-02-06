class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////user.db'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
