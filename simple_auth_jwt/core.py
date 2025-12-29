from simple_auth_jwt.config import AuthConfig, configure
from simple_auth_jwt.jwt_handler import create_access, create_refresh
from simple_auth_jwt.crypto import verify_password

_repo = None

def init(user_repo):
    global _repo
    _repo = user_repo

def login(email: str, password: str):
    if _repo is None:
        raise Exception("UserRepository não inicializado")

    user = _repo.get_by_email(email)
    if not user:
        raise Exception("Usuário não encontrado")

    if not verify_password(user.password, password):
        raise Exception("Senha incorreta")

    access_token = create_access(user.id)
    refresh_token = create_refresh(user.id)
    return {
        "access": access_token,
        "refresh": refresh_token
    }