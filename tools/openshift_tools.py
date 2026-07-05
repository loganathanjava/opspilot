from services.openshift.pods import PodService


def list_pods(namespace: str) -> list[dict]:
    """
    List all pods in an OpenShift namespace.
    """

    service = PodService()

    pods = service.list_pods(namespace)

    return [pod.to_dict() for pod in pods]


def list_unhealthy_pods(namespace: str) -> list[dict]:
    """
    List unhealthy pods in an OpenShift namespace.
    """

    service = PodService()

    pods = service.list_unhealthy_pods(namespace)

    return [pod.to_dict() for pod in pods]