from models.openshift import Pod
from services.openshift.base import BaseService
from services.openshift.mappers import PodMapper
from services.openshift.parsers import PodParser


class PodService(BaseService):

    def list_pods(self, namespace: str) -> list[Pod]:
        """
        Returns all pods in the given namespace.
        """

        response = self.client.get(
            f"/api/v1/namespaces/{namespace}/pods"
        )

        return [
            PodMapper.from_api(item, namespace)
            for item in response.get("items", [])
        ]

    def list_unhealthy_pods(self, namespace: str) -> list[Pod]:
        """
        Returns only unhealthy pods in the given namespace.
        """

        response = self.client.get(
            f"/api/v1/namespaces/{namespace}/pods"
        )

        return [
            PodMapper.from_api(item, namespace)
            for item in response.get("items", [])
            if PodParser.is_unhealthy(item)
        ]