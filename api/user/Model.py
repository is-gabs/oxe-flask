from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    email: str
    _id: str = None

    def dict(self):
        return asdict(self)
    
    def set_id(self, _id: str):
        self._id = _id