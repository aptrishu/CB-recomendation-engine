import os

DEBUG = os.environ.get('DEBUG', True)
SECRET_KEY = os.environ.get('FLASK_SECRET', '23051996')
API_TOKEN = os.environ.get('API_TOKEN', 'TOKEN23')
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
