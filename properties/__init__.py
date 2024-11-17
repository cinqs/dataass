import os

def get(key: str, default_value: str = None):
    return os.environ.get(key, default=default_value)

def __init():
    pass