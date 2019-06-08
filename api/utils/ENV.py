from dataclasses import dataclass
import os


@dataclass
class Env:
    MONGO_URL: str = os.environ.get('MONGO_URL')


envs = Env()