from services.openshift.base import BaseService


class NamespaceDetailsService(BaseService):
    """
    Service for retrieving namespace resources.
    """

    def summary(self, namespace: str) -> dict:

        deployments = self.client.get(
            f"/apis/apps/v1/namespaces/{namespace}/deployments"
        )

        services = self.client.get(
            f"/api/v1/namespaces/{namespace}/services"
        )

        pvc = self.client.get(
            f"/api/v1/namespaces/{namespace}/persistentvolumeclaims"
        )

        events = self.client.get(
            f"/api/v1/namespaces/{namespace}/events"
        )

        return {
            "deployments": len(deployments.get("items", [])),
            "services": len(services.get("items", [])),
            "pvcs": len(pvc.get("items", [])),
            "events": len(events.get("items", [])),
        }