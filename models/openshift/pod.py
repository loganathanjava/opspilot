from dataclasses import dataclass, asdict


@dataclass
class Pod:
    name: str
    namespace: str
    ready: str
    status: str
    restart_count: int
    reason: str
    node: str | None = None
    age: str | None = None

    def to_dict(self) -> dict:
        """Convert the Pod model to a dictionary."""
        return asdict(self)