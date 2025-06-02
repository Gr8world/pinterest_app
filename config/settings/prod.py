from .base import *

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
