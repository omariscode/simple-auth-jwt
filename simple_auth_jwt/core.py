from .crypto import verify_password
from .jwt_handler import create_access, create_refresh

repo = None

def init(user_repository):
    global repo
    repo = user_repository

def login(email, password):
    if not repo:
        raise RuntimeError("Call simple_auth.init() first")

    user = repo.get_by_email(email)
    if not user:
        raise ValueError("Invalid credentials")

    if not verify_password(password, user.password):
        raise ValueError("Invalid credentials")

    return {
        "access": create_access({"sub": user.email}),
        "refresh": create_refresh({"sub": user.email})
    }
