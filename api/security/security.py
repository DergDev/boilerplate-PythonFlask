import config
import functools
from flask import request
from hmac import compare_digest


def is_valid(api_key: str):
    if config.API_KEY is None:
        return True
    if api_key and compare_digest(config.API_KEY, api_key):
        return True
    else:
        return False


def api_key_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if request.headers:
            api_key = request.headers.get("api_key")
        else:
            return {"message": "Please provide an API key"}, 400
        # Check if API key is correct and valid
        if request.method == "POST" or request.method == "DELETE" or request.method == "PATCH" and is_valid(api_key):
            return func(*args, **kwargs)
        else:
            return {"message": "The provided API key is not valid"}, 403

    return decorator
