from fastapi import Request, HTTPException
from simple_auth_jwt.jwt_handler import decode_token

async def auth_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(401, "Missing token")

    decode_token(token.split()[1])
    return await call_next(request)
