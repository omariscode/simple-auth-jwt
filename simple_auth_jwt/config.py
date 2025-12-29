class AuthConfig:
    secret_key = "change-me"
    access_expire_min = 30
    refresh_expire_days = 7

def configure(**kwargs):

    for key, value in kwargs.items():
        if hasattr(AuthConfig, key):
            setattr(AuthConfig, key, value)