# Simple Auth JWT

A simple, plug-and-play JWT authentication SDK for Python web frameworks like Flask and FastAPI. This SDK provides easy-to-use functions for user authentication, token generation, and middleware for protecting routes.

## Features

- JWT token generation (access and refresh tokens)
- Password hashing and verification
- Middleware for FastAPI and Flask to protect routes
- Programmatic configuration
- Lightweight and easy to integrate

## Installation

Install the package via pip:

```bash
pip install simple-auth-jwt
```

Or from source:

```bash
git clone https://github.com/omariscode/simple-auth-jwt.git
cd simple-auth-jwt
pip install .
```

## Quick Start

### 1. Configure the SDK

Configure your JWT settings programmatically:

```python
from simple_auth_jwt import configure

configure(
    secret_key="your-secret-key-here",
    access_expire_min=30,
    refresh_expire_days=7
)
```

### 2. Initialize the SDK

First, you need to provide a user repository that implements a `get_by_email(email)` method returning a user object with `email` and `password` attributes.

```python
from simple_auth_jwt import init, login

# Example user repository (you should implement this)
class UserRepository:
    def get_by_email(self, email):
        # Your logic to fetch user from database
        # Return user object with email and password (hashed)
        pass

# Initialize with your repository
init(UserRepository())
```

### 3. Login and Get Tokens

```python
# Login user
tokens = login("user@example.com", "password123")
print(tokens)
# Output: {"access": "jwt_access_token", "refresh": "jwt_refresh_token"}
```

## Usage with FastAPI

### Protect Routes with Middleware

```python
from fastapi import FastAPI
from simple_auth_jwt.middlewares.fastapi import auth_middleware

app = FastAPI()

# Add middleware to protect all routes
app.middleware("http")(auth_middleware)

@app.get("/protected")
def protected_route():
    return {"message": "This is protected!"}
```

### Full FastAPI Example

```python
from fastapi import FastAPI, HTTPException
from simple_auth_jwt import init, login
from simple_auth_jwt.middlewares.fastapi import auth_middleware

# Initialize SDK
class UserRepo:
    def get_by_email(self, email):
        # Implement your user fetching logic
        return User(email=email, password=hashed_password)

init(UserRepo())

app = FastAPI()
app.middleware("http")(auth_middleware)

@app.post("/login")
def login_endpoint(email: str, password: str):
    try:
        tokens = login(email, password)
        return tokens
    except ValueError:
        raise HTTPException(401, "Invalid credentials")

@app.get("/protected")
def protected():
    return {"data": "secret"}
```

## Usage with Flask

### Protect Routes with Middleware

```python
from flask import Flask
from simple_auth_jwt.middlewares.flask import auth_middleware

app = Flask(__name__)

@app.route("/protected")
@auth_middleware
def protected_route():
    return {"message": "This is protected!"}
```

Note: The Flask is a decorator.

### Full Flask Example

```python
from flask import Flask, request, jsonify
from simple_auth_jwt import init, login

# Initialize SDK
class UserRepo:
    def get_by_email(self, email):
        # Implement your user fetching logic
        return User(email=email, password=hashed_password)

init(UserRepo())

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login_endpoint():
    data = request.get_json()
    try:
        tokens = login(data["email"], data["password"])
        return jsonify(tokens)
    except ValueError:
        return jsonify({"error": "Invalid credentials"}), 401

# Add protection as needed.
```

## Configuration

Configure the SDK using the `configure` function with the following parameters:

- `secret_key`: Secret key for JWT signing (default: "change-me")
- `access_expire_min`: Access token expiration in minutes (default: 30)
- `refresh_expire_days`: Refresh token expiration in days (default: 7)

Example:

```python
from simple_auth_jwt import configure

configure(secret_key="my-secret", access_expire_min=60)
```

## API Reference

### `configure(**kwargs)`

Configure the SDK settings.

- `secret_key`: Secret key for JWT signing
- `access_expire_min`: Access token expiration in minutes
- `refresh_expire_days`: Refresh token expiration in days

### `init(user_repository)`

Initialize the SDK with a user repository.

- `user_repository`: Object with `get_by_email(email)` method

### `login(email, password)`

Authenticate a user and return JWT tokens.

- `email`: User's email
- `password`: User's password
- Returns: Dict with "access" and "refresh" tokens

### Middlewares

- `simple_auth_jwt.middlewares.fastapi.auth_middleware`: FastAPI middleware for token verification
- `simple_auth_jwt.middlewares.flask.auth_middleware`: Flask middleware for token verification

## Dependencies

- `passlib[bcrypt]`: For password hashing
- `python-jose`: For JWT handling
- `fastapi`: For FastAPI integration
- `flask`: For Flask integration

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License