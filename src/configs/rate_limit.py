from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address
import os



limiter = Limiter(key_func=get_remote_address, storage_uri=os.environ.get('REDIS_URL'), default_limits=["10/minute"])