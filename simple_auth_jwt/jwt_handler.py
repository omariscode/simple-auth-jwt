from datetime import datetime, timedelta
from jose import jwt
from simple_auth_jwt.config import AuthConfig

def create_access(user_id: int):
    expire = datetime.utcnow() + timedelta(minutes=AuthConfig.access_expire_min)
    payload = {"sub": user_id, "exp": expire}
    return jwt.encode(payload, AuthConfig.secret_key, algorithm="HS256")

def create_refresh(user_id: int):
    expire = datetime.utcnow() + timedelta(days=AuthConfig.refresh_expire_days)
    payload = {"sub": user_id, "exp": expire}
    return jwt.encode(payload, AuthConfig.secret_key, algorithm="HS256")

def decode_token(token: str):
    return jwt.decode(token, AuthConfig.secret_key, algorithms=["HS256"])
