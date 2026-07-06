from dataclasses import dataclass, field

from models.openshift.container import Container


@dataclass
class PodDetails:
    """
    Detailed pod information.
    """

    name: str
    namespace: str

    status: str
    reason: str

    ready: str
    restart_count: int

    node: str | None
    age: str | None

    pod_ip: str | None
    host_ip: str | None

    service_account: str | None

    qos_class: str | None

    labels: dict = field(default_factory=dict)

    annotations: dict = field(default_factory=dict)

    owner: str | None = None

    containers: list[Container] = field(default_factory=list)