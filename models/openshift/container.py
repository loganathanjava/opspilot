from dataclasses import dataclass


@dataclass
class Container:
    """
    Represents a container inside a pod.
    """

    name: str
    image: str
    ready: bool
    restart_count: int