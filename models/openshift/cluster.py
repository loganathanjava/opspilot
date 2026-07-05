from dataclasses import dataclass, asdict


@dataclass
class ClusterSummary:
    namespaces: int
    pods: int
    running: int
    pending: int
    failed: int
    unhealthy: int
    restarting: int

    def to_dict(self) -> dict:
        return asdict(self)