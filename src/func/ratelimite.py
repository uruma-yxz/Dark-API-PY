import os
from dotenv import load_dotenv
from fastapi import Request
from fastapi.responses import JSONResponse
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi import Limiter

load_dotenv()
url = os.getenv("rate")

limiter = Limiter(key_func=get_remote_address,storage_uri=url)
