from dataclasses import dataclass


@dataclass
class Deployment:
    """
    Deployment summary.
    """

    name: str
    namespace: str
    ready: str
    available: int
    replicas: int
    strategy: str
    age: str