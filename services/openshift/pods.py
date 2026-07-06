from models.openshift import Pod
from services.openshift.base import BaseService
from services.openshift.mappers import PodMapper
from services.openshift.namespaces import NamespaceService
from services.openshift.parsers import PodParser


class PodService(BaseService):
    """
    Service for working with OpenShift Pods.
    """

    def __init__(self):
        super().__init__()
        self.namespace_service = NamespaceService()

    def list_pods(
            self,
            namespace: str | None = None,
    ) -> list[Pod]:
        """
        Returns pods.

        If namespace is None,
        returns pods from every namespace.
        """

        if namespace:
            return self._list_namespace_pods(namespace)

        pods: list[Pod] = []

        namespaces = self.namespace_service.list_namespaces().get(
            "items",
            [],
        )

        for ns in namespaces:

            pods.extend(
                self._list_namespace_pods(
                    ns["metadata"]["name"]
                )
            )

        return pods

    def list_unhealthy_pods(
            self,
            namespace: str,
    ) -> list[Pod]:
        """
        Returns only unhealthy pods.
        """

        return [
            pod
            for pod in self._list_namespace_pods(namespace)
            if PodParser.is_unhealthy(
                {
                    "status": {
                        "phase": pod.status,
                        "containerStatuses": [],
                    }
                }
            )
               or pod.reason != pod.status
        ]

    def get_pod(
            self,
            namespace: str,
            pod_name: str,
    ) -> Pod | None:
        """
        Returns a single pod summary.
        """

        for pod in self._list_namespace_pods(namespace):

            if pod.name == pod_name:
                return pod

        return None

    def get_logs(
            self,
            namespace: str,
            pod_name: str,
            container: str | None = None,
            previous: bool = False,
            tail_lines: int = 500,
    ) -> str:
        """
        Returns pod logs.
        """

        path = (
            f"/api/v1/namespaces/{namespace}"
            f"/pods/{pod_name}/log"
        )

        params = {
            "tailLines": tail_lines,
        }

        if container:
            params["container"] = container

        if previous:
            params["previous"] = "true"

        return self.client.get(
            path,
            params=params,
        )

    def _list_namespace_pods(
            self,
            namespace: str,
    ) -> list[Pod]:
        """
        Returns pods in a namespace.
        """

        response = self.client.get(
            f"/api/v1/namespaces/{namespace}/pods"
        )

        return [
            PodMapper.from_api(
                item,
                namespace,
            )
            for item in response.get(
                "items",
                [],
            )
        ]