from services.openshift.base import BaseService


class PodDetailsService(BaseService):
    """
    Service for retrieving complete pod details.
    """

    def get(
            self,
            namespace: str,
            pod_name: str,
    ):
        """
        Returns the complete OpenShift Pod object.
        """

        return self.client.get(
            f"/api/v1/namespaces/{namespace}/pods/{pod_name}"
        )