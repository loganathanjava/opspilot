from formatters.pod_formatter import PodFormatter

from services.openshift.namespaces import NamespaceService
from services.openshift.pods import PodService


def list_namespaces() -> dict:
    """
    List all namespaces/projects.
    """

    service = NamespaceService()

    namespaces = [
        item["metadata"]["name"]
        for item in service.list_namespaces().get("items", [])
    ]

    return {
        "resource": "namespaces",
        "count": len(namespaces),
        "items": namespaces,
    }


def list_pods(namespace: str) -> dict:
    """
    Return all pods in a namespace.
    """

    service = PodService()

    pods = service.list_pods(namespace)

    items = PodFormatter.format_list(pods)

    return {
        "resource": "pods",
        "namespace": namespace,
        "count": len(items),
        "items": items,
    }


def list_unhealthy_pods(namespace: str) -> dict:
    """
    Return unhealthy pods in a namespace.
    """

    service = PodService()

    pods = service.list_unhealthy_pods(namespace)

    items = PodFormatter.format_list(pods)

    return {
        "resource": "pods",
        "namespace": namespace,
        "count": len(items),
        "items": items,
    }