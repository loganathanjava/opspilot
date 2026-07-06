from models.openshift import Pod
from services.openshift.base import BaseService
from services.openshift.mappers import PodMapper
from services.openshift.namespaces import NamespaceService
from services.openshift.parsers import PodParser


class PodService(BaseService):

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
            if pod.reason != pod.status
        ]

    def get_pod(
            self,
            namespace: str,
            pod_name: str,
    ) -> Pod | None:
        """
        Returns a single pod.
        """

        for pod in self._list_namespace_pods(namespace):

            if pod.name == pod_name:
                return pod

        return None

    def get_logs(
            self,
            namespace: str,
            pod_name: str,
    ) -> str:
        """
        Returns pod logs.
        """

        return self.client.get(
            f"/api/v1/namespaces/{namespace}/pods/{pod_name}/log"
        )

    def _list_namespace_pods(
            self,
            namespace: str,
    ) -> list[Pod]:

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