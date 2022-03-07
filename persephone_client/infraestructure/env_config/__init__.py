import os
import platform
from decouple import Config, RepositoryEnv, config


config = None
SYSTEM = platform.system()


def get_config(base_path: str) -> Config:
    path = os.path.join(base_path, "opt", "envs", "persephone.client.python.lionx.com.br", ".env")
    path = str(path)
    if os.path.exists(path):
        return Config(RepositoryEnv(path))
    else:
        path = os.path.join("/", "app", ".env")
        path = str(path)
        return Config(RepositoryEnv(path))


if SYSTEM == "Linux":
    config = get_config("/")
elif SYSTEM == "Darwin":
    config = get_config("/")
elif SYSTEM == "Windows":
    config = get_config("C:\\")
else:
    raise Exception("Invalid OS")

__all__ = ["config"]
