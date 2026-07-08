from models.openshift import Deployment
from services.openshift.base import BaseService
from services.openshift.mappers import DeploymentMapper
from services.openshift.namespaces import NamespaceService


class DeploymentService(BaseService):
    """
    Service for retrieving deployments.
    """

    def __init__(self):
        super().__init__()
        self.namespace_service = NamespaceService()

    def list_deployments(
            self,
            namespace: str | None = None,
    ) -> list[Deployment]:
        """
        Returns deployments.

        If namespace is None,
        returns deployments from all namespaces.
        """

        if namespace:
            return self._list_namespace_deployments(
                namespace,
            )

        deployments: list[Deployment] = []

        namespaces = self.namespace_service.list_namespaces().get(
            "items",
            [],
        )

        for ns in namespaces:

            deployments.extend(
                self._list_namespace_deployments(
                    ns["metadata"]["name"],
                )
            )

        return deployments

    def _list_namespace_deployments(
            self,
            namespace: str,
    ) -> list[Deployment]:

        response = self.client.get(
            f"/apis/apps/v1/namespaces/{namespace}/deployments"
        )

        return [
            DeploymentMapper.from_api(item)
            for item in response.get(
                "items",
                [],
            )
        ]