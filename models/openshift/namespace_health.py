from dataclasses import dataclass, asdict


@dataclass
class NamespaceHealth:
    name: str
    pods: int
    running: int
    pending: int
    failed: int
    unhealthy: int

    def to_dict(self) -> dict:
        return asdict(self)