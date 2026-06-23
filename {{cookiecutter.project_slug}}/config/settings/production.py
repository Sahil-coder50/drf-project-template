from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': os.getenv('POSTGRES_ENGINE'),
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}


# ========================
# EMAIL
# ========================
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

# ========================
# Celery
# ========================
from celery.schedules import crontab

CELERY_BROKER_URL=os.getenv("REDIS_URL")
CELERY_RESULT_BACKEND=os.getenv("REDIS_URL")
CELERY_ACCEPT_CONTENT=["json"]
CELERY_TASK_SERIALIZER="json"
CELERY_RESULT_SERIALIZER="json"
CELERY_TIMEZONE="UTC"
CELERY_TASK_TRACKED=True
CELERY_TASK_TIME_LIMIT=30*60
CELERY_TASK_SOFT_TIME_LIMIT=25*60
CELERY_WORKER_PREFETCH_MULTIPLIER=1
CELERY_TASK_ACKS_LATE=True
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_REJECT_ON_WORKER_LOST = True
CELERY_RESULT_EXPIRES = 3600
CELERY_TASK_DEFAULT_QUEUE = "default"


# ========================
# Channels
# ========================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
            "capacity": 1500,
            "expiry": 10,
        },
    },
}