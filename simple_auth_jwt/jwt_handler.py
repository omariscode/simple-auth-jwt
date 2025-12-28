from datetime import datetime, timedelta
from jose import jwt
from .config import *

def create_access(payload):
    data = payload.copy()
    data["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_EXPIRE_MIN)
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh(payload):
    data = payload.copy()
    data["exp"] = datetime.utcnow() + timedelta(days=REFRESH_EXPIRE_DAYS)
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
