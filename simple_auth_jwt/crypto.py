from passlib.hash import bcrypt
from simple_auth_jwt.config import AuthConfig

_custom_hasher = None

def use_hasher(hasher):
    global _custom_hasher
    _custom_hasher = hasher

def hash_password(password: str) -> str:
    if _custom_hasher:
        return _custom_hasher.generate_password_hash(password)
    return bcrypt.hash(password)

def verify_password(hash: str, password: str) -> bool:
    if _custom_hasher:
        return _custom_hasher.check_password_hash(hash, password)
    return bcrypt.verify(password, hash)
